# Replace bytearray with correct bytes

x = bytearray([80,75,3,4,20,0,0,0,0,0,72,190,71,0,0,0])


with open('output_bytearray.zip', 'wb') as f:
    # Write the bytearray to the file
    f.write(x)