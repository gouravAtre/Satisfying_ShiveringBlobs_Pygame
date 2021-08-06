# import random

# BLUE = (0, 0, 255)
# class Blob:

#     def __init__(self, color):
#         self.x = random.randrange(0, 200)
#         self.y = random.randrange(0, 300)
#         self.size = random.randrange(4, 8)
#         self.color = color

# blue_blobs = dict(enumerate([Blob(color=BLUE) for i in range(10)]))

# print(blue_blobs)
thisdict = {
  0: "Ford",
  1: "Mustang",
  2: 1964
}

for i in thisdict:
    print(thisdict[i])