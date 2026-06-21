# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37972(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
