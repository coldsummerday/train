#include "ros.h"
#include "std_msgs/String.h"
ros::NodeHandle nh;
std_msgs::String str_msg;
void messageCb(const std_msgs::String&toggle_msg)
{
  Serial.println(toggle_msg.data);
  Serial.println("2");   
}
ros::Subscriber<std_msgs::String> sub("chatter", &messageCb );
void setup()
{
  Serial.begin(9600);
  Serial.println("begin");
  nh.initNode();
  nh.subscribe(sub);
  
}


void loop()
{
  nh.spinOnce();
  delay(1);
}
