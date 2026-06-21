# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest07833(request):
    user_id = request.GET.get('id', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(user_id),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
