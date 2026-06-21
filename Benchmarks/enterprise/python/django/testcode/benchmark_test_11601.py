# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11601(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
