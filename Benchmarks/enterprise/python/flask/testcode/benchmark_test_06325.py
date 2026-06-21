# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest06325():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    return Markup('<div>' + str(data) + '</div>')
