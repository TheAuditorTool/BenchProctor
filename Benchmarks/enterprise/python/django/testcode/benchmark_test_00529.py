# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00529(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
