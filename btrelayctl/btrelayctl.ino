#define PIN_MIN 4
#define PIN_MAX 13

void setup()
{
  // Configure the BT module
  Serial.begin(9600); //set baud rate
  delay(2000);
  Serial.println("AT");
  Serial.readStringUntil('\n');
  Serial.print("AT+NAMELiGhTpAtH");
  Serial.readStringUntil('\n');
  Serial.setTimeout(1000);

  for (int i = PIN_MIN; i < PIN_MAX + 1; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
}

void loop()
{
  String message = Serial.readStringUntil('\n');
  message.trim();

  if (message.length() == 0)
    return;

  if (message.startsWith("BTR")) { // our command
    String cmd, param;
    int p;

    cmd = message.substring(4);
    p = cmd.indexOf(' ');
    if (p == -1)
      param = "";
    else {
      param = cmd.substring(p + 1);
      cmd = cmd.substring(0, p);
    }
    if (cmd == "HIGH") {
      int pin = param.toInt();
      if (pin < PIN_MIN || pin > PIN_MAX) {
        Serial.println("-ERR pin out of scope");
        return;
      }
      digitalWrite(pin, HIGH);
    } else if (cmd == "LOW") {
      int pin = param.toInt();
      if (pin < PIN_MIN || pin > PIN_MAX) {
        Serial.println("-ERR pin out of scope");
        return;
      }
      digitalWrite(pin, LOW);
    }
  }
  Serial.println("+OK");
 }
    

