# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest04651(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
