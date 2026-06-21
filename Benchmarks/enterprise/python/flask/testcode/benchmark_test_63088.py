# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest63088():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
