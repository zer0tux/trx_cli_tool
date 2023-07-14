import struct

def extract_trx(filename, output_dir):
    with open(filename, 'rb') as f:
        data = f.read()

    if len(data) >= 28 and data[4:8] == b"HDR0":
        magic, length, csum, version, offset, tLength = struct.unpack(">4sLLLHH", data[:28])
        image = data[offset:offset+length]
    elif len(data) >= 20 and data[:4] == b"HDR0":
        magic, length, csum, version, offset, tLength = struct.unpack(">4sLLHH", data[:20])
        image = data[offset:offset+length]
    else:
        raise ValueError("Invalid firmware format")

    with open(output_dir + "/image.bin", "wb") as f:
        f.write(image)

    with open(output_dir + "/header.txt", "w") as f:
        f.write("Length: " + str(length) + "\n")
        f.write("Checksum: " + hex(csum) + "\n")
        f.write("Version: " + hex(version) + "\n")
        f.write("Offset: " + str(offset) + "\n")
        f.write("Trailer Length: " + str(tLength) + "\n")

    print("Extraction completed successfully!")

def pack_trx(input_dir, output_file):
    with open(input_dir + "/image.bin", "rb") as f:
        image = f.read()

    length = len(image)
    csum = sum(image) & 0xffffffff
    version = 1
    offset = 32
    tLength = 0

    header = struct.pack(">4sLLHHLL", b"HDR0", length, csum, version, offset, tLength)

    with open(output_file, 'wb') as f:
        f.write(header)
        f.write(b'\0' * (offset - len(header)))
        f.write(image)

    print("Packing completed successfully!")

print ("Chose your side, unpack - 1 or pack - 2 ?")
side = int(input())

if side == 1:
    print ("Hell yeah, unpack all!")
    print ("Write filename:")
    fn = input()
    print ("Set directory:")
    directory = input()
    extract_trx(fn,directory)

elif side == 2:
    print ("Pack!Pack!Pack!Rack!")
    print ("Set input dir:")
    ind = input()
    print ("Write output file:")
    oufile = input()
    pack_trx(ind,oufile)
else:
    print ("You wrong c8mshoot, try again")