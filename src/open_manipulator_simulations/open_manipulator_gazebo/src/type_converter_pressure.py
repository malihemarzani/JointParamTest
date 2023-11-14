#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from bioin_tacto.msg import raw_barometer
from std_msgs.msg import Header

class TypeConverter:

    def __init__(self):
        # Create a subscriber for the first message type
        self.sub_to_first_msg_type = rospy.Subscriber('/open_manipulator/joint_states', JointState, self.first_message_callback)

        # Create a publisher for the second message type
        self.pub_to_second_msg_type = rospy.Publisher('raw_barometer_teensy_sim', raw_barometer, queue_size=10)



    def first_message_callback(self, msg):
    
        header = Header()
        header.stamp = rospy.Time.now() 
        
        # Extract position element from the first message
        position = msg.position[4]

        # Create the second message
        second_msg = raw_barometer()

        # Populate the second message
        second_msg.baro_level = position
        
        second_msg.header = header
        
        # Publish the second message
        self.pub_to_second_msg_type.publish(second_msg)

if __name__ == '__main__':
    rospy.init_node("message_conversion_node")
    TypeConverter()
    rospy.spin()
