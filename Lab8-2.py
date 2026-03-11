source_file = input("Enter source file name: ")
dest_file = input("Enter destination file name: ")

source = open(source_file, "r")
dest = open(dest_file, "w")

for line in source:
    if not line.strip().startswith("#"):
        dest.write(line)

source.close()
dest.close()

print("\nSource File Content:")
print(open(source_file).read())

print("\nDestination File Content:")
print(open(dest_file).read())