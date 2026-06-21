# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest71512(request):
    upload_name = request.FILES['upload'].name
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(upload_name),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
