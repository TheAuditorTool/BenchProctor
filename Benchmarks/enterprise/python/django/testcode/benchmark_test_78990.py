# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest78990(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
