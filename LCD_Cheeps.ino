#include <LiquidCrystal.h>
#include <SimpleDHT.h>

// for DHT11, 
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 2;
SimpleDHT11 dht11;

void setup() {
  Serial.begin(9600);
  // initalize number of rows and col on LCD
  lcd.begin(16,2);
  // print inital message to LCD
  lcd.print("Welcome! Cheeps here.");
}

void loop() {
    
  // read with raw sample data.
  byte temperature = 0;
  byte humidity = 0;
  byte data[40] = {0};
  if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
    Serial.println("X");
    return;
  }
  else{
    Serial.print((int)temperature);
    Serial.print(","); 
    Serial.println((int)humidity); 
  }
  // Cheep section
  if(Serial.available()){
    str[]=Serial.readString();
  }
  lcd.setCursor(0,0);
  lcd.print(str[0]; lcd.print("cheeps");
  lcd.setCursor(0,1);
  lcd.print(str[1]);
  // DHT11 sampling rate is 1HZ.
  delay(1000);
}
