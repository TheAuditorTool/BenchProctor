# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest31794(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    os.remove(str(data))
    return JsonResponse({"saved": True})
