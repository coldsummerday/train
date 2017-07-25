#include "ros.h"
#include "std_msgs/Float64.h"
ros::NodeHandle nh;

int InputPin = 8;
int OutputPin = 9;
void messageCb(const std_msgs::Float64&msg)
{
 
  if(msg.data>1 &&msg.data<2 )
  {
    Forward(1000);
  }
  if (msg.data>2 && msg.data<3)
  {
    Back(1000);
  }
  if (msg.data>3 && msg.data<4)
  {
    Left(1000);
  }
  if (msg.data >4 && msg.data<5)
  {
    Right(1000);
  }
  if(msg.data>5 && msg.data<6)
  {
    FirstPoint();
  }
  if(msg.data >6 && msg.data<7)
  {
    SecondPoint();
  }
  if (msg.data>7 && msg.data<8)
  {
    ThirdPoint();
  }
  if (msg.data >8 && msg.data<9)
  {
    ForthPoint();
  }
  if (msg.data>9)
  {
   
    Stop(1000);
  }
 
  
    
}
ros::Subscriber<std_msgs::Float64> sub("chatter", &messageCb );
void setup()
{
  nh.initNode();
  nh.subscribe(sub);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(InputPin,INPUT);
  pinMode(OutputPin,OUTPUT);
  
}


void loop()
{
  nh.spinOnce();
  digitalWrite(OutputPin,LOW);
  delayMicroseconds(2);
  digitalWrite(OutputPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(OutputPin,LOW);
  int distance = pulseIn(InputPin,HIGH);
  distance = distance/58;
  delay(50);
  if(distance >= 30)
  {
    Forward(500);
  }
  else
  {
    Stop(40);
  }
}

void FirstPoint()
{
  Forward(2000);
  Right(1500);
  Forward(9000);
  Stop(2000);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
  
}

void SecondPoint()
{
   Forward(2000);
   Right(1500);
   Forward(15000);
   Stop(2000);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
}

void ThirdPoint()
{
  Forward(2000);
  Right(1500);
  Forward(20000);
  Stop(2000);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
}

void ForthPoint()
{
  Forward(11500);
  Right(1500);
  Forward(8000);
  Stop(4000);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
}

void Back(int a)
{
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(7,LOW);
  
}

void Forward(int a)
{
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(7,HIGH);
  delay(a);
}

void Left(int a)
{
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
  digitalWrite(7,HIGH);
  delay(a);
}

void Right(int a)
{
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,LOW);
  delay(a);
}

void Stop(int a)
{
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
  delay(a);
}


