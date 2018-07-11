#Decode.py
print("")

data = "021C01450900020000498E0000000000004C2200000000000000000000000000000000006402570000007E32380A12070401FF016300210001000100050002000500010514"
print(len(data))
data_spl = [data[i:i+2] for i in range(0, len(data), 2)]
#data_hex = [data[i:i+2] for i in range(0, len(data), 2)]
data_int = [int(data[i:i+2],16) for i in range(0, len(data), 2)]
#print(data_spl)
print(data_int)
#print(type(data_spl[0]))

print(hex(sum(data_int)&0xFF))

data2 = "021C0145290002000049C00000000000004C540000000000000000000000C9000000CB006402570001007E39040B12070401FF016F0042000100010005000200050001072E"
print(len(data2))
data2 = "021C0145290002000058CA0000000000005C30000000000000003C000000C5000000CE005602570001007D1F180B12070401FF018C00A5000100010005000200"
print(len(data2))
data_spl2 = [data2[i:i+2] for i in range(0, len(data2), 2)]
data_int2 = [int(data2[i:i+2],16) for i in range(0, len(data2), 2)]
#print(hex(126))
#print(data_spl2)
print(data_int2)
print(hex(sum(data_int2)&0xFF))

for i in range(len(data_int2)):
    print("%03d %03d"%(data_int[i],data_int2[i]))
