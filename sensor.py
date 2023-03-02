from smbus import SMBus

class IRSeeker360():
	def __init__(self,port:int):
		self.port = port if type(port) == int else int(port[-1])

		self.i2c_address = 0x08

		self.create_bus()

	def read(self):
		# Read infrared sensor bin data from all 12 sensors
		raw_ir = [self.bus.read_i2c_block_data(self.i2c_address, i, 2) for i in range(12)]

		# Fix invalid read data
		all_angles = [value for value in raw_ir[0] if 0 <= value <= 12]

		# return Angle, Strength
		return max(set(all_angles), key = all_angles.count), max(set(raw_ir[1]), key = raw_ir[1].count)

	def create_bus(self):
		self.bus = SMBus(self.port + 0x2)

	def close(self):
		self.bus.close()
