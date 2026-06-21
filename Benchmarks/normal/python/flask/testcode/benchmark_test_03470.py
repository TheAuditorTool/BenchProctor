# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03470():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return render_template_string(data)
