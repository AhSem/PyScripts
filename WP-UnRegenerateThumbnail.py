import os
import datetime

start = datetime.datetime.now()
print('Start:', start)

directory = "C:\\Users\\Chang Chin Sem\\Desktop\\2018\\09"

ext = [".png", ".jpg", ".jpeg"]

max_width = 1200
max_height = 1200

count = 0

for filename in os.listdir(directory):
	for width in range(29, max_width):
		for height in range(29, max_height):
			for e in ext:
				if filename.endswith('-' + str(width) + 'x' + str(height) + e):
					print(str(datetime.datetime.now()) + '---' + os.path.join(directory, filename))

					try:
						os.remove(filename)
						count = count + 1
					
					except Exception as error:
						print('Error:', error)

					continue
				else:
					continue

print(str(count) + ' files are deleted.')

end = datetime.datetime.now()
print('End:', end)

print('Duration', end-start)