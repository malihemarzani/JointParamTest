#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from bioin_tacto.msg import raw_imu
from std_msgs.msg import Header

def first_message_callback(msg):

    header = Header()
    header.stamp = rospy.Time.now() 
    
    # Extract elements from the first message
    orientation_x = msg.orientation.x
    orientation_y = msg.orientation.y
    orientation_z = msg.orientation.z

    ang_vel_x = msg.angular_velocity.x
    ang_vel_y = msg.angular_velocity.y
    ang_vel_z = msg.angular_velocity.z

    linear_acc_x = msg.linear_acceleration.x
    linear_acc_y = msg.linear_acceleration.y
    linear_acc_z = msg.linear_acceleration.z

    # Create and populate the second message
    second_msg = raw_imu()
    second_msg.mx = orientation_x
    second_msg.my = orientation_y
    second_msg.mz = orientation_z

    second_msg.ax = ang_vel_x
    second_msg.ay = ang_vel_y
    second_msg.az = ang_vel_z

    second_msg.gx = linear_acc_x
    second_msg.gy = linear_acc_y
    second_msg.gz = linear_acc_z
    
    second_msg.header = header

    # Create a publisher for the second message type
    second_msg_pub = rospy.Publisher('raw_imus_teensy_sim', raw_imu, queue_size=10)

    # Publish the second message
    second_msg_pub.publish(second_msg)

def main():
    rospy.init_node('message_conversion_node')

    # Create a subscriber for the first message type
    first_msg_sub = rospy.Subscriber('imu', Imu, first_message_callback)

    rospy.spin()

if __name__ == '__main__':
    main()
