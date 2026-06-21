# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest40293(request):
    user_id = request.GET.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
