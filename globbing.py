import glob
import shutil
file = glob.glob("files/*.docx")
print(file)


shutil.make_archive("output", "zip", "files")