
import math
import socket
import struct
import time
import threading
from scipy.spatial.transform import Rotation as R














# For for tomorrow:

def bytes_to_drone_info(bytes_telemetry: bytearray):
 
    lenght = len(bytes_telemetry)
    print (f"Bytes Lenght: {lenght} bytes")
    
    if lenght ==101:
        player_index = struct.unpack('<i', bytes_telemetry[0:4])[0]
        timestamp = bytes_telemetry[4:8]
        position_x = bytes_telemetry[8:12]
        position_y = bytes_telemetry[12:16]
        position_z = bytes_telemetry[16:20]
        quaternion_x = bytes_telemetry[20:24]
        quaternion_y = bytes_telemetry[24:28]
        quaternion_z = bytes_telemetry[28:32]
        quaternion_w = bytes_telemetry[32:36]

        drone_position_x = struct.unpack('f', position_x)[0]
        drone_position_y = struct.unpack('f', position_y)[0]
        drone_position_z = struct.unpack('f', position_z)[0]
        drone_quaternion_x = struct.unpack('f', quaternion_x)[0]
        drone_quaternion_y = struct.unpack('f', quaternion_y)[0]
        drone_quaternion_z = struct.unpack('f', quaternion_z)[0]
        drone_quaternion_w = struct.unpack('f', quaternion_w)[0]

        # Convert quaternion to Euler angles
        quat = [drone_quaternion_x, drone_quaternion_y, drone_quaternion_z, drone_quaternion_w]
        if all(q == 0 for q in quat):
            # print("Warning: Quaternion is all zeros, skipping Euler conversion.")
            drone_euler_x = drone_euler_y = drone_euler_z = 0.0
        else:
            r = R.from_quat(quat)
            euler_rad = r.as_euler('yxz', degrees=False)
            drone_euler_x, drone_euler_y, drone_euler_z = [math.degrees(angle) for angle in euler_rad]

            #inverse y and x
            temp_value = drone_euler_x
            drone_euler_x = drone_euler_y
            drone_euler_y = temp_value
        bool_is_defender  = player_index==1
        print(f"Player Index: {player_index} {'(Defender)' if bool_is_defender else '(Attacker)'}")
        print(f"Timestamp: {struct.unpack('<I', timestamp)[0]}")
        print(f"Position: ({drone_position_x}, {drone_position_y}, {drone_position_z})")
        print(f"Quaternion: ({drone_quaternion_x}, {drone_quaternion_y}, {drone_quaternion_z}, {drone_quaternion_w})")
        print(f"Euler Angles: ({drone_euler_x}, {drone_euler_y}, {drone_euler_z})")
        print("Drone info processed successfully.")
    elif lenght == 4: # has no drone id
        print(f"Received telemetry data with length {lenght} bytes, but no drone info to process.")
# Xomi Gamepad Control UDP settings 

      






xomi_gamepad_to_control_port = 3615
xomi_gamepad_to_control_ipv4 = "127.0.0.1"


def push_integer_to_xomi_gamepad_control(int_value_to_push: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        try:
            print (f"Pushing integer value {int_value_to_push} to Xomi Gamepad Control at {xomi_gamepad_to_control_ipv4}:{xomi_gamepad_to_control_port}")
            udp_socket.sendto(struct.pack('<i', int_value_to_push), (xomi_gamepad_to_control_ipv4, xomi_gamepad_to_control_port))
        except socket.error as e:
            print(f"Error sending data: {e}")

def percent_to_int_1_99(percent:float)-> int:
    if percent == 0:
        return 0
    
    value = 1 + int( (percent+1.0) /2.0 * 98.0) 
    if value < 1:
        return 1
    elif value > 99:
        return 99
    else:
        return value


def push_gamepad_joystick(float_left_x, float_left_y, float_right_x, float_right_y):
    """
    Pushes the gamepad joystick values to the server.
    
    :param float_left_x: Left joystick X-axis value
    :param float_left_y: Left joystick Y-axis value
    :param float_right_x: Right joystick X-axis value
    :param float_right_y: Right joystick Y-axis value
    """
    int_value_left_x = percent_to_int_1_99(float_left_x)*1000000
    int_value_left_y = percent_to_int_1_99(float_left_y)*10000
    int_value_right_x = percent_to_int_1_99(float_right_x)*100
    int_value_right_y = percent_to_int_1_99(float_right_y)*1
    int_value_to_push = 100000000 + int_value_left_x + int_value_left_y + int_value_right_x + int_value_right_y
    push_integer_to_xomi_gamepad_control(int_value_to_push)

  


def loop_listen_to_telemetry_with_drone_index():
    """
    This function listens to telemetry data and processes it.
    It is a placeholder for your code.
    """
    print("Listening to telemetry data...")

    udp_listen_port = 9002  # Example port, change as needed
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind(('0.0.0.0', udp_listen_port))
        print(f"Listening for UDP packets on port {udp_listen_port}...")
        # Placeholder for actual telemetry listening logic
        while True:
            data, client_address = udp_socket.recvfrom(1024)
            bytes_telemetry = bytearray(data)
            int_player_index = struct.unpack('<i', bytes_telemetry[:4])[0]
            print(f"Received telemetry data from player index: {int_player_index}")

            bytes_to_drone_info(bytes_telemetry)

            print("Processing telemetry data...")  # Replace with actual processing logic


def loop_insert_your_code_here():
    # This function is a placeholder for your code.
    # You can replace this with the actual code you want to run.
    print("Insert your code here.")

    jValue = 0.6
    while True:
        
        time.sleep(1)
        push_gamepad_joystick(0,0,0,0)
        time.sleep(1)
        push_gamepad_joystick(0,-1,0,0)
        time.sleep(1)
        push_gamepad_joystick(-jValue,0,0,0)
        time.sleep(1)
        push_gamepad_joystick(jValue,0,0,0)
        time.sleep(1)
        push_gamepad_joystick(0,-jValue,0,0)
        time.sleep(1)
        push_gamepad_joystick(0,jValue,0,0)
        time.sleep(1)
        push_gamepad_joystick(0,0,-jValue,0)
        time.sleep(1)
        push_gamepad_joystick(0,0,jValue,0)
        time.sleep(1)
        push_gamepad_joystick(0,0,0,-jValue)
        time.sleep(1)
        push_gamepad_joystick(0,0,0,jValue)
        time.sleep(1)
        push_gamepad_joystick(0,0,0,0)
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=loop_insert_your_code_here, daemon=True)
    t2 = threading.Thread(target=loop_listen_to_telemetry_with_drone_index, daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()







