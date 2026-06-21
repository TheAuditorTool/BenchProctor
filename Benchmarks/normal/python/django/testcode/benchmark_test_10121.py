# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest10121(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
