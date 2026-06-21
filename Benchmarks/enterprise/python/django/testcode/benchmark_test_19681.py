# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest19681(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    reader = make_reader(referer_value)
    data = reader()
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
