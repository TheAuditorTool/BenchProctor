# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest27091(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
