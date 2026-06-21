# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest54465(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
