# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest67920(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
