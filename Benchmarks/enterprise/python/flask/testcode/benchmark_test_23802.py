# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23802():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
