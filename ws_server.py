#!/bin/python3.6

import asyncio
import websockets
import argparse


from kafka import KafkaConsumer

import conf as co

camera_id = []

parser = argparse.ArgumentParser()
parser.add_argument('port', metavar='port', type=int, help='tcp port')
parser.add_argument('camera_id', metavar='camid', type=str, nargs='+',help='list of id dim.camera')
consumer = KafkaConsumer('events',bootstrap_servers=co.ka_host, auto_offset_reset='latest')


async def SendEvt(websocket,path):
    for m in consumer:
        if m.value.decode().split(":")[2] in camera_id:
            await websocket.send(m.value.decode())
            print("sent event %s" % m.value.decode())


if __name__ == "__main__":

    args = parser.parse_args()
    camera_id = args.camera_id
    start_server = websockets.serve(SendEvt, '0.0.0.0', args.port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()