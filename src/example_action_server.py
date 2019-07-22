#! /usr/bin/env python

import rospy

import actionlib

import action_server_example.msg

class ExampleAction(object):
	_result = action_server_example.msg.OpenCloseResult()


	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, 
		action_server_example.msg.OpenCloseAction, execute_cb=self.execute_cb,
		auto_start = False)

		self._as.start()

	def execute_cb(self, goal):
		#helper variables
		r = rospy.Rate(1)
		success = True

		rospy.loginfo('%s: Executing, returning boolean value of %i' %(self._action_name,
		goal.request))

		if self._as.is_preempt_requested():
                	rospy.loginfo('%s: Preempted' % self._action_name)
                	self._as.set_preempted()
                	success = False
                		


		if success:
			#check request string and call functions to open and close gripper
			#gripper = Robotiq_Two_Finger_Gripper(robot, 1.25)
			#then return true
			#if(request = 'close') --> robotiqgrip.close_gripper()
			#if(request = 'open') --> robotiqugrip.open_gripper()
			#rob.send_program(robotiqgrip.ret_program_to_run())
				#rob.close()
				#print "true"
				#sys.exit()
			self._result.OpenOrClose = goal.request
			rospy.loginfo('%s: Succeeded' % self._action_name)
	            	self._as.set_succeeded(self._result)
		


if __name__ == '__main__':
	rospy.init_node('OpenClose')
	server = ExampleAction(rospy.get_name())
	rospy.spin()
			
