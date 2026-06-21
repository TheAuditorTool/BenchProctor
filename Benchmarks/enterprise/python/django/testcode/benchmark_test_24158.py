# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest24158(request):
    upload_name = request.FILES['upload'].name
    random.seed(int(upload_name) if str(upload_name).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
