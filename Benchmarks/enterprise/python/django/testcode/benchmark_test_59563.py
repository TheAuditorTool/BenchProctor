# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest59563(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = FormData(payload=prop_value).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
