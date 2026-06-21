# SPDX-License-Identifier: Apache-2.0
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56423(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
