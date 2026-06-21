# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09632(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    int(str(data))
    return JsonResponse({"saved": True})
