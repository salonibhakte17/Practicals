source = open("input.txt", "r")
destination = open("output.txt", "w")

data = source.read()
destination.write(data.upper())

source.close()
destination.close()

print("Content copied in uppercase.")