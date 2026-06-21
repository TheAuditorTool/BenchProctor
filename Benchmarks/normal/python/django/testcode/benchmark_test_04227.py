# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest04227(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
