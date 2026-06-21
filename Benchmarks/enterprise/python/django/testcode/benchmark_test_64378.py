# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest64378(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
