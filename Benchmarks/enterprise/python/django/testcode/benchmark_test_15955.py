# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15955(request):
    user_id = request.GET.get('id', '')
    exec(str(user_id))
    return JsonResponse({"saved": True})
