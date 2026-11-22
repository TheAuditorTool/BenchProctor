# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00233(request):
    field_value = request.POST.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(field_value).strip()
        case _:
            data = str(field_value)
    request.session.update({'data': str(data)})
    return JsonResponse({"saved": True})
