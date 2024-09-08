from xarm.wrapper import XArmAPI
import time

ip = '172.23.254.167'

arm = XArmAPI(ip)
arm.motion_enable(enable=True, servo_id=8)
arm.set_mode(0)
arm.set_state(0)

arm.reset(wait=True)

speed = 50
arm.set_servo_angle(angle=[-0.1, -2.5, 78.8, 0.4, 71.6, 35.2], speed=50)
# arm.set_position(250)
# arm.move_gohome()

arm.close_lite6_gripper()
time.sleep(5)
arm.open_lite6_gripper()