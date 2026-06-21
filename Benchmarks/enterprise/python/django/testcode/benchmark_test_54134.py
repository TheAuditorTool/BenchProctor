# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest54134(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
