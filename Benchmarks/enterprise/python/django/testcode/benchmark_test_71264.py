# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71264(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
