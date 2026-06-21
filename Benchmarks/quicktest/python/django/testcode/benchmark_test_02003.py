# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02003(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
