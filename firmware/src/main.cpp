#include "WiFi.h"

void setup() {
  Serial.begin(115200);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(5, OUTPUT);
  // delay(1000);  // Allow time for Serial monitor to connect
  // WiFi.mode(WIFI_STA);  // Set WiFi to station mode
  // Serial.println("ESP32 S3 WiFi Scanner Started");
}

bool state = false;

void loop() {

  int value = analogRead(A0);
  Serial.println(value);
  value = analogRead(A1);
  Serial.println((3.3f * value) / 4095.0f * 3.2f);
  digitalWrite(5, state);
  state = !state;
  // Serial.println("\nScanning for WiFi networks...");

  // int n = WiFi.scanNetworks();
  // if (n == 0) { 
  //   Serial.println("No networks found.");
  // } else {
  //   Serial.printf("%d network(s) found:\n", n);
  //   for (int i = 0; i < n; ++i) {
  //     Serial.printf("%d: %s (RSSI: %d) %s\n", i + 1,
  //                   WiFi.SSID(i).c_str(),
  //                   WiFi.RSSI(i),
  //                   (WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? "Open" : "Encrypted");
  //   }
  // }

  // // Clean up to free memory
  // WiFi.scanDelete();

  delay(2000);  // Wait 1 second before the next scan
}


// #include "SHT85.h"

// uint32_t start;
// uint32_t stop;

// SHT30 sht1(0x44);


// void setup()
// {
//   //  while(!Serial);  //  uncomment if needed
//   Serial.begin(115200);
//   Serial.println();
//   Serial.println(__FILE__);
//   Serial.print("SHT_LIB_VERSION: \t");
//   Serial.println(SHT_LIB_VERSION);
//   Serial.println();

//   Wire.begin();
//   Wire.setClock(100000);
//   sht1.begin();

//   Serial.println("\nCONNECT");
//   Serial.println(sht1.isConnected());

//   Serial.println("\nSTATUS");
//   uint16_t stat = sht1.readStatus();
//   Serial.print(stat, HEX);
//   Serial.println();
//   Serial.print(stat, HEX);
//   Serial.println();

//   delay(1000);
// }


// void loop()
// {
//   start = micros();
//   sht1.read();         //  default = true/fast       slow = false
//   stop = micros();
//   Serial.print("SHT1:\t");
//   Serial.print((stop - start) * 0.001);
//   Serial.print("\t");
//   Serial.print(sht1.getTemperature(), 1);
//   Serial.print("\t");
//   Serial.println(sht1.getHumidity(), 1);
//   delay(1000);
// }
