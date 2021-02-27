from time import sleep
from rsmq import RedisSMQ

time_input_queue = RedisSMQ(host='redis-clusterip-srv', qname="time_input_queue")
time_output_queue = RedisSMQ(host='redis-clusterip-srv', qname="time_output_queue")