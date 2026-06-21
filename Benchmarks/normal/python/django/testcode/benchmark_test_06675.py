# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06675(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
