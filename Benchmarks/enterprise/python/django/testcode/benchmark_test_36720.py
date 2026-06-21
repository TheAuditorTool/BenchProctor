# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36720(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
