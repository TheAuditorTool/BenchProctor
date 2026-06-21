# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest49202(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
