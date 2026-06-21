# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06438(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
