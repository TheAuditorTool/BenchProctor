# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest10575():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
