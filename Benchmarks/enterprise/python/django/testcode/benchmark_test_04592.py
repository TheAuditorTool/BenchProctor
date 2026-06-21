# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04592(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
