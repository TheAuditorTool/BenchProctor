# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest23468(request):
    xml_value = request.body.decode('utf-8')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(xml_value),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
