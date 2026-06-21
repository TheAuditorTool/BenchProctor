# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest00415(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
