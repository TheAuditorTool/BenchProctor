# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest28152(request):
    upload_name = request.FILES['upload'].name
    entries = os.listdir(str(upload_name))
    return JsonResponse({'listing': entries}, status=200)
