length = float(input('Length (meters): '))
width = float(input('Width (meters): '))
height = float(input('Height (meters): '))

circumference = 2*(length+width)
volume = length*width*height
wall_area = 2*(width*height)+2*(length*height)
n_of_windows = int(2*(wall_area/26.3))
needed_paint = (wall_area - 2*n_of_windows)*0.75

print(f"Circumference: {circumference:.2f} meters")
print(f"Volume: {volume:.2f} cubic meters")
print(f"Wall area: {wall_area:.2f} square meters")
print(f"Number of windows: {n_of_windows}")
print(f"Needed paint: {needed_paint:.2f} liters")
