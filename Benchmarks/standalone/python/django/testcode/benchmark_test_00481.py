# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00481(request):
    host_value = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(host_value).strip()
        case _:
            data = str(host_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
