# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest00797(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
