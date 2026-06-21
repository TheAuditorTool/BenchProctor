# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest78422(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
