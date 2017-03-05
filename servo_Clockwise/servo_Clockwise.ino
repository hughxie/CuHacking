#include <Servo.h> 
 
int servoPin = 8;
 
Servo servo;  
 
 
void setup() 
{ 
  servo.attach(servoPin); 
} 
 
 
void loop() 
{ 
  
  servo.write(0);
  

} 
