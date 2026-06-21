# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest27672(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
