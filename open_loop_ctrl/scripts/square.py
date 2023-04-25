#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("square")

    pub=rospy.Publisher("/cmd_vel",Twist, queue_size=10)
    cmd_vel = Twist()

    kpt = 1 
    kpr = 1

    v = 0.5 
    w = 0.5
    
    distance = 0
    ang_distance = 0

    rate = rospy.Rate(10)    
    
    tI = rospy.get_time()
    while not rospy.is_shutdown():
        
        for i in range(1, 6):

            while(distance < 2):
                cmd_vel.linear.x = v*kpt
                cmd_vel.angular.z = 0

                pub.publish(cmd_vel)

                dt = rospy.get_time() - tI
                distance = distance + (dt * abs(v))

                tI = rospy.get_time()
                rate.sleep()

            distance = 0

            while(ang_distance < (3.1416/2)):
                cmd_vel.linear.x = 0
                cmd_vel.angular.z = w*kpr

                pub.publish(cmd_vel)

                dt = rospy.get_time() - tI
                ang_distance = ang_distance + (dt * abs(w))

                tI = rospy.get_time()
                rate.sleep()
            
            ang_distance = 0


        cmd_vel.linear.x = 0
        cmd_vel.angular.z = 0
        pub.publish(cmd_vel)
