#include <WiFi.h>

#include "constants.hpp"

// Replace with your STA (client) credentials
const char* ssid_sta = "Your_STA_SSID";
const char* password_sta = "Your_STA_Password";

// Replace with your AP credentials
const char* ssid_ap = "ESP32_AP";
const char* password_ap = "12345678";

void setup() {
  Serial.begin(115200);

  // Set the ESP32 to both AP and STA mode
  WiFi.mode(WIFI_AP_STA);

  // Start STA (connect to existing Wi-Fi)
  WiFi.begin(ssid_sta, password_sta);
  Serial.println("Connecting to WiFi (STA)...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to STA network.");
  Serial.print("STA IP address: ");
  Serial.println(WiFi.localIP());

  // Start AP
  bool result = WiFi.softAP(ssid_ap, password_ap);
  if (result) {
    Serial.println("Access Point started.");
    Serial.print("AP IP address: ");
    Serial.println(WiFi.softAPIP());
  } else {
    Serial.println("Failed to start Access Point.");
  }
}

void loop() {
  // Your code here
}
