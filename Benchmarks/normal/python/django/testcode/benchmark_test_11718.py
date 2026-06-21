# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11718(request):
    user_id = request.GET.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
