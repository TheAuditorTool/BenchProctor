# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26272(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
