# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64851():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return Markup('<div>' + str(data) + '</div>')
