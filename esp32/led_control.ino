#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "wifi_name";
const char* password = "wifi_password";
const char* mqtt_server = "X.X.X.X"; //Raspberry Pi IP 

WiFiClient espClient;
PubSubClient client(espClient);

const int ledPin = 19; //using pin19 on esp32

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.println(topic);

  String msg;
  for (int i = 0; i < length; i++) msg += (char)payload[i];

  Serial.print("Message: ");
  Serial.println(msg);

  if (msg == "tvmonitor detected") {
    Serial.println("Triggering LED!");
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
      client.subscribe("camera/events");
      Serial.println("Subscribed to camera/events");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 2 seconds");
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  Serial.println("\nConnected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();  
}
