# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest53192(request):
    user_id = request.GET.get('id', '')
    logging.info('User action: ' + str(user_id))
    return JsonResponse({"saved": True})
