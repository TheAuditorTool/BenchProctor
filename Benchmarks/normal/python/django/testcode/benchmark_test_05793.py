# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05793(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
