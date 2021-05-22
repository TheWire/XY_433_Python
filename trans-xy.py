import argparse
from XY_433 import XY_4333_trans

parser = argparse.ArgumentParser(description='')
parser.add_argument('pin', type=int, help='Raspberry Pi Broadcom GPIO pin number')
parser.add_argument('code', type=int, help='Command to transmit')
parser.add_argument('-b', '--bits', type=int, default=24, help='Number of bits in command')
parser.add_argument('-r', '--repeat', type=int, default=5, help='Number of repeated transmissions')
args = parser.parse_args()
trans = XY_433_trans(arg.pin)

trans.XY_send(args.code, args.bits, args.repeat)
print("transmission successfull")