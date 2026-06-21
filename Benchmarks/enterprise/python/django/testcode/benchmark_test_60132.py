# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest60132(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
