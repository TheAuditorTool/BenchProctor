# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60071(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
