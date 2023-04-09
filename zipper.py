import zipfile
import pathlib

def zip_filer(filepath, destination_directory):
    dest_path = pathlib.Path(destination_directory, "compressed_files.zip")
    with zipfile.ZipFile(dest_path, 'w') as f:

        for path in filepath:
            file_path = pathlib.Path(path)
            f.write(path, arcname=file_path.name)


# if __name__ == "__main__":
