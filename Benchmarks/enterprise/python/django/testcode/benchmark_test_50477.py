# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest50477(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
