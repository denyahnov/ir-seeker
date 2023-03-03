# 360 IR Seeker - Building Block Robotics
### Official Website: https://irseeker.buildingblockrobotics.com/
![](https://3854067563-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fwumhy9Amexb1fvjNOGl8%2Fuploads%2FGAIFGoCIqSNBC1NGZRd5%2FIR%20Seeker%20-%20v1-2%202%20.jpg?alt=media)

## Setup
Here is a [video tutorial](https://youtu.be/G23W2WtwAIw) if needed
 1. Download the latest firmware from [here](https://irseeker.buildingblockrobotics.com/updates/latest-version)
 2. Plug the IR board into your computer using Micro USB
 3. Find the reset button on the board
 4. Double press the reset button.
 5. If you have pressed the button correctly, you will see a new USB drive appear on your computer. This drive will be called `BBSBOOT`.
 6. Copy the firmware update to this drive. (no need to rename file)
 7. The IR board will restart and the USB drive will disappear. It’s now ready to be used on your robot again.
 8. Connect the IR board to your EV3 brick like any other sensor 
 
## Building your robot
`45 Degree - Yellow Holes`
`90 Degree - Red Holes`
> **Note:** Do not mix these holes or you may break the board

![](https://user-images.githubusercontent.com/60083582/222574224-28a1a3c3-0c22-4469-9c6b-1e1b0e48eb03.png)

## Writing code
### Copy this class into your code
```python
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
```
### Implementing into your code
```python
# Change '1' to whatever port you are using
ir_board = IRSeeker360(1)

# This will return a ball angle (0 to 12) and strength
angle, strength = ir_board.read()
```
