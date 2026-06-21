# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37045(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
