# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest27345(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
