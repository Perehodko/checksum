import hashlib
from hashlib import md5, sha1, sha256
import sys


def receive_arguments():
    try:
        path_to_file, path_to_dir = sys.argv[1], sys.argv[2]
        return path_to_file, path_to_dir
    except IndexError as e:
        print("Arguments: {}!".format(e))
        raise SystemExit


def count_and_check_checksum(path_to_file, path_to_dir):
    try:
        with open(path_to_file) as f:
            for line in f:
                line = line.rstrip()
                file_name, algorithm, etalon_hash = line.split()

                try:
                    if algorithm == "md5":
                        real_hash = hashlib.md5(open(path_to_dir + file_name, "rb").read()).hexdigest()
                    elif algorithm == "sha1":
                        real_hash = sha1(open(path_to_dir + file_name, "rb").read()).hexdigest()
                    elif algorithm == "sha256":
                        real_hash = hashlib.sha256(open(path_to_dir + file_name, "rb").read()).hexdigest()

                    if etalon_hash == real_hash:
                        print(file_name, "OK")
                    else:
                        print(file_name, "FAIL")

                except FileNotFoundError:
                    print(file_name, "NOT FOUND")
    except ValueError:
        print("Ошибка. Проверьте корректность файла checksum_for_files.txt")


path_to_file, path_to_dir = receive_arguments()
count_and_check_checksum(path_to_file, path_to_dir)