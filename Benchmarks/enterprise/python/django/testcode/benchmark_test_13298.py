# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest13298(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    logging.info('User action: ' + str(auth_header))
    return JsonResponse({"saved": True})
