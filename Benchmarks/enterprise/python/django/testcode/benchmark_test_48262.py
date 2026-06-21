# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest48262(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
