import zipfile
import pathlib

def make_archive(filepaths,destination_dir):
    archived_file = pathlib.Path(destination_dir,'compressed.zip')
    with zipfile.ZipFile(archived_file,mode='w') as zip:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath,arcname=filepath.name)


#for testing this file
if __name__ == "__main__":
    filepaths = ['c.txt', 'a.txt']
    destination_dir = ''
    make_archive(filepaths,destination_dir)

