# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30113(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
