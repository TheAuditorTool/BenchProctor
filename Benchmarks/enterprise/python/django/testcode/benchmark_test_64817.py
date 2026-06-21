# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64817(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
