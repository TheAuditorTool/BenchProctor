# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest32288(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = FormData(payload=query_array).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
