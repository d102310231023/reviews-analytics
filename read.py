data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

sumlength = 0
for d in data:
	sumlength =sumlength + len(d)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))		
