import time
import math

class Simulator:
	def __init__(self):
		self.amplitude = pow(10,-3)
		self.frequency = 1

	def sin_wave(self):
		t = time.time()
		frequency = self.frequency
		amp = self.amplitude
		phase = 0
		value = amp*math.sin(frequency*t+phase)
		return t, value;

	def cos_wave(self):
		t = time.time()
		frequency = self.frequency
		amp = self.amplitude
		phase = 0
		value = amp*math.cos(frequency*t+phase)
		return t, value;
		
	def get(self):
		dat1 = self.sin_wave()
		dat2 = self.cos_wave()
		dat3 = math.sqrt(dat1[1]**2+dat2[1]**2)

		return dat1, dat2, dat3;
	
