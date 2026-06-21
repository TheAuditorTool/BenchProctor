# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest76636(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
