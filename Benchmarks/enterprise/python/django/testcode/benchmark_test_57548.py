# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest57548(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
