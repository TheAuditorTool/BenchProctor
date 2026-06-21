# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


def BenchmarkTest62762():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
