# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81109(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
