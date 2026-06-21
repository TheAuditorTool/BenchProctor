# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31305(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    eval(str(data))
    return JsonResponse({"saved": True})
