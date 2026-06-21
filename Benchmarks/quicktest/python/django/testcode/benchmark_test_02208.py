# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest02208(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
