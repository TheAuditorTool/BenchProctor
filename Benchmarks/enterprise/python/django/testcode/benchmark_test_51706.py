# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest51706(request):
    multipart_value = request.POST.get('multipart_field', '')
    random.seed(int(multipart_value) if str(multipart_value).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
