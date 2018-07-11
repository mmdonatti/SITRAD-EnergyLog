import serial
import time
from serial import rs485

ser = serial.Serial(port='COM2', baudrate=28800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_MARK, stopbits=serial.STOPBITS_ONE, timeout=3, xonxoff=False, rtscts=False, dsrdtr=False)

#ser.rs485_mode = serial.rs485.RS485Settings()
#ser.open()

for i in range(0):

    ser. reset_input_buffer()
    ser. reset_output_buffer()

    ser.parity=serial.PARITY_MARK
    #ser.rts = 1
    #ser.dtr = 0

    cmd="\xfa"
    ser.write(cmd)
    print(cmd.encode('hex'))
    #msg=ser.read(64)
    #print(msg)

    ser.parity=serial.PARITY_SPACE
    #ser.rts = 1
    cmd="\x40"
    ser.write(cmd)
    print(cmd.encode('hex'))
    #msg=ser.read(64)
    #print(msg)

    #ser.rts = 1
    cmd="\x04"
    ser.write(cmd)
    print(cmd.encode('hex'))
    #msg=ser.read(64)
    #print(msg)

    #ser.rts = 1
    cmd="\x00"
    ser.write(cmd)
    print(cmd.encode('hex'))
    #msg=ser.read(64)
    #print(msg)

    #ser.rts = 1
    cmd="\x00"
    ser.write(cmd)
    print(cmd.encode('hex'))
    #msg=ser.read(64)
    #print(msg)

    #ser.rts = 1
    cmd="\xfe"
    ser.write(cmd)
    print(cmd.encode('hex'))

    #ser.rts = 0
    print("Reading...")
    msg=ser.read(64)
    print(msg.encode('hex'))

t_msg = time.time()
delay_send = 1
#ser.reset_input_buffer()
#ser.reset_output_buffer()

try:
    while(True):
        if time.time() - t_msg >= delay_send:
            t_msg = time.time()
            #ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.rts = 1
            time.sleep(70.0/1000.0)
            #ser.parity = serial.PARITY_SPACE
            #ser.rts = 1
            #ser.dtr = 0
            ser.parity = serial.PARITY_MARK
            #ser.rts = 1

            cmd="\x02"
            ser.write(cmd)
            print(cmd.encode('hex'))
            #ser.dtr = 0
            ser.parity = serial.PARITY_SPACE
            cmd="\x20"
            ser.write(cmd)
            print(cmd.encode('hex'))
            time.sleep(70.0/1000.0)
            ser.rts = 0
            #ser.rts = 0

        if ser.in_waiting > 0:
            msg=ser.read(69)
            data = msg.encode('hex')
            data_split_hex = [data[i:i+2] for i in range(0, len(data), 2)]
            data_split_int = [int(data[i:i+2],16) for i in range(0, len(data), 2)]
            print("Data Length: "+str(len(data)))
            print(data_split_int)
            if len(data)==138:
                print("Voltage: "+str(data_split_int[-27])+" V\n\n")

except KeyboardInterrupt:
    print("Keyboard Interrupt... closing COM port")
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.close()
