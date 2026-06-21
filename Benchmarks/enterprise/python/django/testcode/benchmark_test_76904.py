# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76904(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    int(str(data))
    return JsonResponse({"saved": True})
