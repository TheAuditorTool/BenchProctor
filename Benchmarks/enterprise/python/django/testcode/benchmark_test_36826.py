# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest36826(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(referer_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
