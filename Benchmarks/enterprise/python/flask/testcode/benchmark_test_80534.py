# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest80534():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    return Markup('<div>' + str(data) + '</div>')
