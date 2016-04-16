String message; //string that stores the incoming message

void setup()
{
  Serial.begin(9600); //set baud rate
  delay(2000);
  Serial.println("AT");
  Serial.readStringUntil('\n');
  Serial.println("AT+NAMELiGhTpAtH");
  Serial.readStringUntil('\n');
  Serial.setTimeout(1000);
}

void loop()
{
  String message = Serial.readStringUntil('\n');
  message.trim();

  if (message.length() == 0)
    return;
    
  Serial.println(message);
 }
    

