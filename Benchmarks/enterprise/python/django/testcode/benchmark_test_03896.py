# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest03896(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    def _primary():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
