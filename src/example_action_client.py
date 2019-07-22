#! /usr/bin/env python

from __future__ import print_function
import rospy


# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import action_server_example.msg

def example_client():
	# Creates the SimpleActionClient, passing the type of the action
   	# (FibonacciAction) to the constructor.
   	client = actionlib.SimpleActionClient('OpenClose', action_server_example.msg.OpenCloseAction)

	#wait until the action server has been started and is listening for goals	
	client.wait_for_server()

	#creates a goal to send to the action server 
	goal = action_server_example.msg.OpenCloseGoal(request=False)

	#send the goal to the action server 
	client.send_goal(goal)

	#wait for server to finish the action
	client.wait_for_result()

	#print out the result
	return client.get_result()

if __name__ == '__main__':
	try:
		#initializes a node so the client can publish and subscribe using ROS
		rospy.init_node('example_client_py')
		result = example_client()
		print("Result:", result.OpenOrClose)
	except rospy.ROSInterruptException:
        	print("program interrupted before completion", file=sys.stderr)
