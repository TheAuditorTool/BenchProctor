# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01550(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
