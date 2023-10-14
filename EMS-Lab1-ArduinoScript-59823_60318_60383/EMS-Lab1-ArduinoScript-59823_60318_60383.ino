#include <math.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define sensor_pin_NTC 34  
#define sensor_pin_LM35 35 // LM35 is connected to this PIN
#define ONE_WIRE_BUS 26

float VDD = 5;
//NTC
float R1 = 1800;
float R2 = 1200;
float R3 = 10000;
float R4 = 1800;
float R2_R3 = (R2*R3) / (R2+R3);
float A = 1.120446846E-3;
float B = 2.365502706E-4;
float C = 0.7086713122E-7;
//LM35
float R2_LM35 = 100;
float R3_LM35 = 2000;
float R4_LM35 = 1200;
float R2_R3_LM35 = (R2_LM35*R3_LM35) / (R2_LM35+R3_LM35);

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  sensors.begin();
  Serial.begin(115200);
}

void loop() {
  
  //NTC
  //float voltage_NTC = 3.15;
  float voltage_NTC = analogRead(sensor_pin_NTC) * (3.3 / 4096);
  float NTC = ( (R1*VDD*((R2_R3 + R4)/R2_R3)) / (voltage_NTC + R4*VDD/R3) ) - R1;
  float temperature_NTC = 1 / ( A + B * log(NTC) + C*pow((log(NTC)),3)) - 273.15;
  //Serial.print("Temperature_NTC: ");
  //Serial.print(temperature_NTC);
  //Serial.println(" C ");
  
  //LM35
  //float voltage_out = 3.25;
  float voltage_out = analogRead(sensor_pin_LM35) * (3.3 / 4096);
  float voltage_LM35 = ( voltage_out + R4_LM35*VDD/R3_LM35)*(R2_R3_LM35/(R2_R3_LM35+R4_LM35));
  float temperature_LM35 = voltage_LM35 * 100;
  //Serial.print("Temperature_LM35: ");
  //Serial.print(temperature_LM35);
  //Serial.println(" C ");
  
  //DS18B20
  sensors.requestTemperatures();
  float temperature_DS18B20 = sensors.getTempCByIndex(0);
  //float temperature_DS18B20 = digitalRead(ONE_WIRE_BUS);
  //Serial.print("Temperature_DS18B20: ");
  //Serial.print(temperature_DS18B20);
  //Serial.println(" C ");

  Serial.print(temperature_NTC);
  Serial.print(" ");
  Serial.print(temperature_LM35);
  Serial.print(" ");
  Serial.println(temperature_DS18B20);
  
  delay(1000);
}