# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from rest_framework import serializers


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00154(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    reader = make_reader(referer_value)
    data = reader()
    class _InputSerializer(serializers.Serializer):
        value = serializers.RegexField("^[a-zA-Z0-9 _.%\\-]+$")
    _ser = _InputSerializer(data={'value': str(data)})
    if not _ser.is_valid():
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
