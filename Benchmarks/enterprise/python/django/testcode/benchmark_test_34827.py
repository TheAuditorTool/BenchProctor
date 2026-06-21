# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34827(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    int(str(data))
    return JsonResponse({"saved": True})
