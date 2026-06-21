# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest10012(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
