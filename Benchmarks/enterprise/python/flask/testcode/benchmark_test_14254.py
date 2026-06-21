# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14254():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    return Markup('<div>' + str(data) + '</div>')
