# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest03830(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    int(str(data))
    return JsonResponse({"saved": True})
