# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47939(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    int(str(data))
    return JsonResponse({"saved": True})
