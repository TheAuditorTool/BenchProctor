# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07359(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
