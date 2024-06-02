import can
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 500000
from can.interface import Bus

bus = Bus()

with can.Bus() as bus:
    for msg in bus:
        print(msg.data)
