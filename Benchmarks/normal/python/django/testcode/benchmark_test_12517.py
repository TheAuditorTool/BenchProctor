# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12517(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
