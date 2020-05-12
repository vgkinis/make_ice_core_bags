import numpy as np

bag1 = 15
bag2 = 2705
ppag = 5
bag_length = 0.55

samples = np.arange(1,ppag+1)
bags = np.arange(bag1, bag2+1)
f = open("./make_bags_out.txt", "w")
for bag_i in bags:
	for sample_i in samples.astype(int):
		depth_i = bag_i*bag_length - bag_length + sample_i*bag_length/ppag
		string_out = "%i\t%i\t%0.3f\n" %(bag_i, sample_i, depth_i)
		print(string_out)
		f.write(string_out)

f.close()
