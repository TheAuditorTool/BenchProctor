# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest03145():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
