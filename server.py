import asyncio
import websockets
import rospy
from move_base_msgs.msg import MoveBaseActionGoal

async def server(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message: {message}")

        #Transform message to position
        if message == '1':
            # enter position where you want to make the robot move
            publish_rostopic_command(-0.587, 2.892, 0.177, 0.984)
            response = "Command 1 sent to the robot"
        else:
            response = "Invalid command"

        await websocket.send(response)

def publish_rostopic_command(x, y, z, w):
    rospy.init_node('rostopic_publisher', anonymous=True)
    pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)
    rospy.loginfo("Publishing rostopic command...")
    
    # Create a MoveBaseActionGoal message with the desired values
    move_base_msg = MoveBaseActionGoal()
    move_base_msg.goal.target_pose.header.stamp = rospy.Time.now()
    move_base_msg.goal.target_pose.header.frame_id = 'map'
    move_base_msg.goal.target_pose.pose.position.x = x
    move_base_msg.goal.target_pose.pose.position.y = y
    move_base_msg.goal.target_pose.pose.position.z = 0.0
    move_base_msg.goal.target_pose.pose.orientation.x = 0.0
    move_base_msg.goal.target_pose.pose.orientation.y = 0.0
    move_base_msg.goal.target_pose.pose.orientation.z = z
    move_base_msg.goal.target_pose.pose.orientation.w = w

    pub.publish(move_base_msg)
    rospy.loginfo("Command published")

async def run_server():
    # Replace {YOUR_IP} with your IP address.
    # example 192.11.22.33
    # 8080 is port number. You can change it if you want
    async with websockets.serve(server, {YOUR_IP}, 8080):
        print("Server is running...")
        await asyncio.Future()  # Keep the server running

asyncio.get_event_loop().run_until_complete(run_server())
