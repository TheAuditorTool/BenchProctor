# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00520(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    form = FormData(payload=origin_value)
    data = form.payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
