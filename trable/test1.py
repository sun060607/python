import serial as pyserial

def openSerial(port, baudrate=9600,bytesize=pyserial.EIGHTBITS, parity=pyserial.PARITY_NONE, stopbits=pyserial.STOPBITS_ONE,timout=None,
               xonxonff=False, rtscts=False, dsrdtr=False):
    ser = pyserial.Serial()

    ser.port=port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity=parity
    ser.stopbits = stopbits
    ser.timout = timout
    ser.xonxonff = xonxonff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr

    ser.open()
    return ser

def writePort(ser,data):
    ser.write(data)

def writePortUnicode(ser,data):
    writePort(ser,data.encode())

def read(ser,size=1, timeout=None):
    ser.timeout = timeout
    readed = ser.read(size)
    return readed

def readUntilExitCode(ser, exitcode=b'\x03'):
    readed = b''
    while True:
        data = ser.read()
        print(data)
        readed += data
        if exitcode in data:
            return readed[:1]

def readEOF(ser):
    readed = ser.readline()
    return readed[:-1]

def handler(signum, frame):
    print("program end!")

def readThread(ser):
    while True:
        if ser.readable():
            readed = ser.readline()
            print(readed[:-1])


if __name__ == '__main__':
    
    ser = openSerial('com17')
    string = 'hello world\n'
    writePort(ser,string.encode())
    writePortUnicode(ser,string)

    string = b'Hello World\n'
    writePort(ser,string)

    string = "안녕\r\n"
    writePortUnicode(ser,string)

    readed = read(ser)
    print(readed)
    print(readEOF(ser))
    print(readUntilExitCode(ser))