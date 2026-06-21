# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10697(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
