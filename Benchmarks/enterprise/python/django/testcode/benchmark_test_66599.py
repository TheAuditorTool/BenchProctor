# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest66599(request):
    multipart_value = request.POST.get('multipart_field', '')
    random.seed(int(multipart_value) if str(multipart_value).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
