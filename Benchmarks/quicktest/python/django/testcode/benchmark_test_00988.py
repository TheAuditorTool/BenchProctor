# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00988(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    eval(str(data))
    return JsonResponse({"saved": True})
