# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00137(request):
    field_value = request.POST.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
