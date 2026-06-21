# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75374(request):
    user_id = request.GET.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
