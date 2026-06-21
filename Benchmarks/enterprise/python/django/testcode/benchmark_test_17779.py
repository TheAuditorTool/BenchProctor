# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17779(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
