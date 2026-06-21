# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00075(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    reader = make_reader(referer_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
