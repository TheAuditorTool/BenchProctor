# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest41968():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    return Markup('<div>' + str(data) + '</div>')
