# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50288(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
