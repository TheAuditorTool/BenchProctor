# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote
from app_runtime import db


def BenchmarkTest04383(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
