# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00095(request):
    field_value = request.POST.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session.update({'data': str(processed)})
    return JsonResponse({"saved": True})
