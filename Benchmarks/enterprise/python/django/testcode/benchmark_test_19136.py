# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest19136(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
