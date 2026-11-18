# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
import base64
from app_runtime import db


def BenchmarkTest00458(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
