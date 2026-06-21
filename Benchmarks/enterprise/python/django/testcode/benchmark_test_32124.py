# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest32124(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    os.remove(str(data))
    return JsonResponse({"saved": True})
