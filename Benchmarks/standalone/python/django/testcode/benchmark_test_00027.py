# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import MD4
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00027(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    digest = MD4.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
