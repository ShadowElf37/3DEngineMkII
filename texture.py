from sys import stderr

class ImageData:
	def __init__(self, w, h, dat):
		self.width = self.w = w
		self.height = self.h = h
		self.data = dat

def load_tex(name):
	try:
		fle = open("textures/" + str(name) + ".csi", 'r')
	except FileNotFoundError:
		print("Error: " + str(name) + ".csi was not found in the textures folder.", file=stderr)
		raise FileNotFoundError
	output = []
	(wid, hei) = [int(i) for i in fle.readline().split(' ')]
	for line in fle:
		if line[0] == '#':
			continue
		cols = line.split(',')
		output.append([("#%02x%02x%02x" % tuple([int(i) for i in c.split(' ')])) for c in cols])
		#print([("#%02x%02x%02x" % tuple([int(i) for i in c.split(' ')])) for c in cols])
	del fle
	return ImageData(wid, hei, output)

