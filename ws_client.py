#!/bin/python3.6
import asyncio
import websockets
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('ip', metavar='ip', type=str, help='ip address')
parser.add_argument('port', metavar='port', type=int, help='tcp port')


async def ResvEvt(ip,port):
    async with websockets.connect('ws://{}:{}'.format(ip,port)) as websocket:
        while True:
            evt = await websocket.recv()
            print(evt)




if __name__ == "__main__":

    args = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(ResvEvt(args.ip,args.port))
