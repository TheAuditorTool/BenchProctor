# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72536(request):
    user_id = request.GET.get('id', '')
    if not str(user_id).isdigit():
        raise Exception('error: ' + str(user_id))
    return JsonResponse({"saved": True})
