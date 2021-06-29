char ch  ='0';
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2,OUTPUT);//clock
  pinMode(3,OUTPUT);//PWM
  pinMode(4,OUTPUT);

  pinMode(7,OUTPUT);//clock
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);//PWM
}


void stop_car()
{ 
  //Serial.println("stop");
  digitalWrite(2, LOW); 
  digitalWrite(4, LOW); 
  digitalWrite(7, LOW); 
  digitalWrite(8, LOW); 
  

}
void fast_reverse()
{
  analogWrite(3, 255); 
  analogWrite(9, 255); 
  //Serial.println("fast_F");
  digitalWrite(2, HIGH); 
  digitalWrite(4, LOW); 
  digitalWrite(7, HIGH); 
  digitalWrite(8, LOW); 
  //delay(3000);
} 
void slow_reverse()
{ 
  analogWrite(3, 150); 
  analogWrite(9, 150); 
  //Serial.println("slow_F");
  digitalWrite(2, HIGH); 
  digitalWrite(4, LOW); 
  digitalWrite(7, HIGH); 
  digitalWrite(8, LOW); 
  //delay(3000);
  
} 
void fast_forward()
{ 
  analogWrite(3, 255); 
  analogWrite(9, 255); 
 // Serial.println("Fast_R");
  digitalWrite(2, LOW); 
  digitalWrite(4, HIGH); 
  digitalWrite(7, LOW); 
  digitalWrite(8, HIGH); 
  //delay(3000); 
} 
void slow_forward()
{ 
  analogWrite(3, 150); 
  analogWrite(9, 150); 
  //Serial.println("slow_R");  
  digitalWrite(2, LOW); 
  digitalWrite(4, HIGH); 
  digitalWrite(7, LOW); 
  digitalWrite(8, HIGH); 
  //delay(3000); 
} 
void right()
{ 
  analogWrite(9, 255); 
  //Serial.println("left");
  digitalWrite(2, HIGH); 
  digitalWrite(4, LOW); 
  digitalWrite(7, LOW); 
  digitalWrite(8, LOW); 
  //delay(3000);
  
} 
void left()
{ 
  analogWrite(3, 255); 
  //Serial.println("Right");
  digitalWrite(2, LOW); 
  digitalWrite(4, LOW); 
  digitalWrite(7, HIGH); 
  digitalWrite(8, LOW); 
  //delay(3000);

} 

void loop(){
  if(Serial.available() > 0)  
  {
    char input = Serial.read();

      if (input == 'a'){
        fast_forward();
      }else if (input == 'b'){
        slow_forward();
      }else if(input == 'c'){
        fast_reverse();
      }else if(input == 'd'){
        slow_reverse();
      }else if(input == 'e'){
        right();
      }else if(input == 'f'){
        left();
      }else if(input == 'g'){
        stop_car();
      }else{
        stop_car();
      }
    
  }

          
     
}
