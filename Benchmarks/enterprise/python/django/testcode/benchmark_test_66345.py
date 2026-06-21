# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest66345(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
