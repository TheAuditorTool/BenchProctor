# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest71114():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    return Markup('<div>' + str(data) + '</div>')
