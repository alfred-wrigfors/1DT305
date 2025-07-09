#include <WiFi.h>
#include <WiFiClient.h>
#include "SHT85.h"

#include "constants.hpp"

const int PIN_WATER   = A0;
const int PIN_BATTERY = A1;

float water     = 0;
float air       = 0;
float humid     = 0;
float voltage   = 0;
float soc       = 0;

void init();
void setup_wifi();
void read_sensors();
bool send_data();
void enter_sleep();

float calc_temp(int adc);
float calc_voltage(int adc);
float calc_soc(float voltage);

WiFiClient    client;
SHT30               sht(0x44);

void setup() { 

    init();

    setup_wifi();
}

void loop() {

    read_sensors();

    send_data();

    enter_sleep();
}

void init(){
    Wire.begin();
    Wire.setClock(100000);
    sht.begin();
    sht.isConnected();
    sht.readStatus();
    int status = sht.isConnected();
    status = sht.readStatus();

    pinMode(PIN_WATER, INPUT);      // PT Sensor
    pinMode(PIN_BATTERY, INPUT);    // Battery Voltage
}

void setup_wifi(){
    WiFi.begin(SSID, PASSWORD);
    while (WiFi.status() != WL_CONNECTED) { delay(500); }
}

void read_sensors(){
    for (size_t i = 0; i < 2; i++)
    {
        sht.read();
        delay(50);
    }    

    water   = calc_temp(analogRead(PIN_WATER));
    voltage = calc_voltage(analogRead(PIN_BATTERY));
    soc     = calc_soc(voltage);
    air     = sht.getTemperature();
    humid   = sht.getHumidity();
}


bool send_data(){

    if (!client.connect(SERVER, PORT)) { return false; }

    // Construct full URL path with query
    String url = "/" + String(ENDPOINT)  +  "?" + 
        "water=" + String(water, 2) + "&" +
        "air=" + String(air, 2) + "&" +
        "humid=" + String(humid, 2) + "&" +
        "voltage=" + String(voltage, 2) + "&" +
        "soc=" + String(soc, 2);


    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
        "Host: " + SERVER + "\r\n" +
        "Connection: close\r\n\r\n");

    // Wait for response headers to end
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") { break; }
    }

    // Read body
    String response = client.readString();

    if (response != "True"){ return false; }

    client.stop();

    return true;
}

void enter_sleep(){
    esp_sleep_enable_timer_wakeup(10 * 1000000);
    esp_deep_sleep_start();
}

float calc_temp(int adc){
    return (float)adc * TEMP_COEFF + TEMP_OFFSET;
}

float calc_voltage(int adc){
    return (float)adc / 4095 * 3.3 * BAT_COEFF;
}

float calc_soc(float voltage){
    return 100.0f * (voltage - BAT_MIN) / (BAT_MAX - BAT_MIN);
}