# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest24444(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
