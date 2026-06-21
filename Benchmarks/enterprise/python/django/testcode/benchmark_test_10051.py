# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest10051(request):
    user_id = request.GET.get('id', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(user_id).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
