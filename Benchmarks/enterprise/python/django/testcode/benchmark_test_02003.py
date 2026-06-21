# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02003(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
