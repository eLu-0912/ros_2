import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "countup", 10)
n = 0


def cb():
    global n
    msg = Person()
    msg.name = "原島偉"
    msg.data = n
    pub.publish(msg)
    n += 1

def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
