# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest73203(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
