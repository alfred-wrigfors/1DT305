#include "WiFi.h"

void setup() {
  Serial.begin(115200);
  delay(1000);  // Allow time for Serial monitor to connect
  WiFi.mode(WIFI_STA);  // Set WiFi to station mode
  Serial.println("ESP32 S3 WiFi Scanner Started");
}

void loop() {
  Serial.println("\nScanning for WiFi networks...");

  int n = WiFi.scanNetworks();
  if (n == 0) {
    Serial.println("No networks found.");
  } else {
    Serial.printf("%d network(s) found:\n", n);
    for (int i = 0; i < n; ++i) {
      Serial.printf("%d: %s (RSSI: %d) %s\n", i + 1,
                    WiFi.SSID(i).c_str(),
                    WiFi.RSSI(i),
                    (WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? "Open" : "Encrypted");
    }
  }

  // Clean up to free memory
  WiFi.scanDelete();

  delay(1000);  // Wait 1 second before the next scan
}
