# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21983(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
