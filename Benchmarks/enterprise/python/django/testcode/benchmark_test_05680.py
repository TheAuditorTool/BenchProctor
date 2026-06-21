# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest05680(request):
    multipart_value = request.POST.get('multipart_field', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(multipart_value),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
