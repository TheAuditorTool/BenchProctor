# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from urllib.parse import unquote


def BenchmarkTest26259(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
