# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19573(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
