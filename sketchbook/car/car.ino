#include "ros.h"
#include "std_msgs/Float64.h"
ros::NodeHandle nh;
#include "DualVNH5019MotorShield.h"

DualVNH5019MotorShield md;

void messageCb(const std_msgs::Float64&msg)
{
 
  if(msg.data>1 &&msg.data<2 )
  {
    Forward(200,2);
  }
  if (msg.data>2 && msg.data<3)
  {
    Back(200,2);
  }
  if (msg.data>3 && msg.data<4)
  {
    Left(200,2);
  }
  if (msg.data >4 && msg.data<5)
  {
    Right(200,2);
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
   
    Stop(2);
  }
 
  
    
}
ros::Subscriber<std_msgs::Float64> sub("chatter", &messageCb );
void setup()
{
  nh.initNode();
  nh.subscribe(sub);
  md.init();
  
}


void loop()
{
  nh.spinOnce();
 
}

void Forward(int speed,int second)
{
    md.setM1Speed(-speed);
    md.setM2Speed(speed);
    delay(second);
}
void Back(int speed,int second)
{
    md.setM1Speed(speed);
    md.setM2Speed(-speed);
    delay(second);
}
void Left(int speed,int second)
{
    md.setM1Speed(speed);
    md.setM2Speed(speed);
    delay(second);
}
void Right(int speed,int second)
{
    md.setM1Speed(-speed);
    md.setM2Speed(-speed);
    delay(second);
}

void Stop(int second)
{
  md.setM1Speed(0);
  md.setM2Speed(0);
  delay(second);
}
void FirstPoint()
{
    Stop(1000);
  Forward(400,2500);
  Left(400,600);
  Forward(400,5000);
  Stop(3000);
}

void SecondPoint()
{
    Stop(1000);
  Forward(400,2500);
  Left(400,600);
  Forward(400,9000);
  Stop(3000);
}

void ThirdPoint()
{
  Stop(1000);
  Forward(400,2500);
  Left(400,600);
  Forward(400,13000);
  Stop(3000);
}

void ForthPoint()
{
  Stop(1000);
  Forward(400,8000);
  Left(400,650);
  Forward(400,5000);
  Stop(3000);
  
}

