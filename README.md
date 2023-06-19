# robot_communication

## Summary
This repository is for communication between different platforms using WebSocket. The purpose of this repository is to open a server on a Linux-based platform and run a client on other platforms (Windows, Mac, Android) to send messages to Linux. The messages are then converted to ROS coordinates and sent as commands to control the robot through ROS topics. In other words, it helps to control the robot from other platforms. For more details, please refer to this [YouTube video](https://youtu.be/7_lBd4AszNM) and [Notion](https://www.notion.so/robotiz/Smart-Fulfillment-Center-8be6ed65c21d49b2bb9968b0afbfb8cf). In the video, the implementation allows controlling the robot by pressing buttons in an app.

## Set up
1. This environment requires Python 3.x or later.
   - For Windows: Download from the [Python official website](https://www.python.org/downloads/).
   - For macOS:
     ```
     brew install python
     ```
   - For Linux:
     ```
     sudo apt-get install python3
     ```

2. Install asyncio:
   ```
   pip install asyncio
   ```

3. Install websockets:
   ```
   pip install websockets
   ```

4. (for the server) Install ROS. Refer to the [ROS official website](http://wiki.ros.org/Distributions) for installation instructions. (In this version, Linux 18.04 LTS and Melodic was used. Therefore, the operation on other platforms or distributions is not guaranteed.)

## Overview
- 'server.py' is a server that receives messages and converts them into coordinates to send move commands to the robot using a topic.
- 'client.py' is a client for testing the communication. It is a simple client that sends any input to the server.

Please run the server and client on the desired platforms.

## How to Run
1. Connect to the same Wi-Fi network. Please note that it may not work on networks with certain security, such as those in secure company or institutional environments. It is recommended to use a personal network.

2. Clone this repository to your desired location.
```
git clone https://github.com/khu-wafer/robot_communication
```

3. Navigate to the downloaded repository and modify the {YOUR_IP} in server.py and client.py. Replace {YOUR_IP} with your actual IP address. For example, if your IP address is 123.45.6.78, replace {YOUR_IP} with 123.45.6.78

4. Modify the messages and coordinates in server.py according to your needs. For example, if you want the robot to move to specific coordinates when receiving the message '1', modify the code as follows:
```python
if message == '1':
    publish_rostopic_command(-0.587, 2.892, 0.177, 0.984)
```
You can refer to the [SLAM Repository](https://github.com/khu-wafer/robot_slam) for robot coordinates.

### Server
5-1. Run roscore.
```
roscore
```

5-2. Open a terminal, navigate to the location of server.py, and run the server. If the following message appears, the server is running successfully.
```
python server.py
```
<p align="center">
<img src="/images/server_1.png" width="450" />
</p>

### Client
5-3. Open a terminal, navigate to the location of client.py, and run the client. If the following message appears, the client is running successfully.
```
python client.py
```
<p align="center">
<img src="/images/client_1.png" width="450" />
</p>

5-4. Enter the message you want to send.
<p align="center">
<img src="/images/client_2.png" width="450" />
</p>

### Server
5-5. If the message is successfully received, the server will display the message as shown below.
<p align="center">
<img src="/images/server_2.png" width="450" />
</p>

## Disclaimer
This code is compatible with Python 3 or higher.
The code has been tested on Windows, macOS, Android, and Linux platforms. It may not work on other platforms, so appropriate modifications may be necessary.

## Credits
[Jinyeob Kim](https://github.com/JinnnK)

## Contact
If you have any questions or find any bugs, please feel free to open an issue or pull request.
