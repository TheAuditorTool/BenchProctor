# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest57695():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    return Markup('<div>' + str(data) + '</div>')
