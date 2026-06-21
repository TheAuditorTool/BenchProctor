# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def normalise_input(value):
    return value.strip()

def BenchmarkTest41040(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
