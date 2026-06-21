# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import base64


def BenchmarkTest71447(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
