# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62801(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    eval(str(data))
    return JsonResponse({"saved": True})
