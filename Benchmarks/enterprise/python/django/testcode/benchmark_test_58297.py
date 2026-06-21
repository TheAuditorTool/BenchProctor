# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest58297(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
