import os
import shutil
import mmap
import re
import pathlib


__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


def clean_cache():
    created_cache = os.path.abspath('.') + r"\cache"
    try:
        os.makedirs("cache", exist_ok=False)
    except FileExistsError:
        shutil.rmtree(created_cache, ignore_errors=False, onerror=None)
        os.makedirs("cache", exist_ok=True)
    # return created_cache  # kan weg?


def cache_zip(zip_file_path, cache_dir_path):
    return shutil.unpack_archive(zip_file_path, cache_dir_path)


def cached_files():
    created_cache = os.path.abspath('.') + r"\cache"
    return [os.path.join(created_cache, file) for file in list(os.walk(created_cache))[0][2]]  # kan korter met ZipFile.namelist()


def find_password(list_of_file_paths):
    words = ['laptop', 'password']
    password_in_file = dict()
    for file_string in list_of_file_paths:
        with open(file_string, 'rb', 0) as file:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            file_name = (pathlib.Path(file_string)).stem
            try:
                match = (([value for word in words if (value := re.search(word.encode("utf-8"), s, re.IGNORECASE))][0]).group()).decode('ascii')
                password_in_file[file_name] = match
            except IndexError:
                return "no matches"
    return password_in_file.values()


# print(clean_cache())                                                                                              # TEST 1
# cache_zip(zip_file_path=r"C:/Xfer/winc/DA/files/data.zip", cache_dir_path=r"C:/Xfer/winc/DA/cache")               # TEST 2
# print(cached_files())                                                                                             # TEST 3
# print(find_password(list_of_file_paths=['C:\\Xfer\\winc\\DA\\cache\\0.txt', 'C:\\Xfer\\winc\\DA\\cache\\1.txt'])) # TEST 4

