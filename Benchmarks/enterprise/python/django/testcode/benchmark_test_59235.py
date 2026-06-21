# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59235(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
