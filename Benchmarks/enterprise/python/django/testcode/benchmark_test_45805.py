# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45805(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
