# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45377(request):
    user_id = request.GET.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
