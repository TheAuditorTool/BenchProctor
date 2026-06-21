# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30875(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    int(str(data))
    return JsonResponse({"saved": True})
