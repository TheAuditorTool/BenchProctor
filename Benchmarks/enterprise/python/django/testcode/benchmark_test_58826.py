# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest58826(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    os.remove(str(data))
    return JsonResponse({"saved": True})
