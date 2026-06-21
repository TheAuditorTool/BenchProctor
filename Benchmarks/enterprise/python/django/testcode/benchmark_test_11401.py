# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11401(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
