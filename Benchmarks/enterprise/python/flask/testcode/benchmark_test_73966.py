# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73966():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
