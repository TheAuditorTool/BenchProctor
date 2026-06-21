# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26521(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
