# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62159(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
