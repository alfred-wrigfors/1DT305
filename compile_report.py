import sys
import os

OUTPUT_NAME = "report.md"
DIRECTORY   = "docs"

output      = ""

output += "<!-- AUTO GENERATED -->\n"

files = os.listdir(DIRECTORY)
files = [file for file in files if ".md" in file and file[0] in "1234567890"]

print("Found files:")

for file in files:
    print("\t" + file)
    with open(os.path.join(DIRECTORY, file)) as f:
        output += "\n<!-- "
        output += file
        output += " -->\n"
        for line in f:
            output += line
        
        output += "\n"

print("Writing output")
with open(OUTPUT_NAME, "w") as f:
    f.write(output)

print("Compilation complete")