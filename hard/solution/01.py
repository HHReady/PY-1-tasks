import os
import hashlib
import collections


def duplicate_files(path):
    hash_dict = collections.defaultdict(list)

    for root, _dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)

            with open(file_path) as f:
                contents = f.read()
                hash_value = hashlib.sha1(contents).hexdigest()
                hash_dict[hash_value].append(file_path)

    return [v for v in hash_dict.values() if len(v) > 1]
