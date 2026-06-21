# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05130(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
