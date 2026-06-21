# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest74030(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
