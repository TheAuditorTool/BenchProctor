# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03996(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    reader = make_reader(referer_value)
    data = reader()
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
