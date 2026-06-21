# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest55084(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
