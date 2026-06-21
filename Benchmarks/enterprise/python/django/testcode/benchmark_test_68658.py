# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest68658(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
