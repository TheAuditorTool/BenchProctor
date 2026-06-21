# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66498(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
