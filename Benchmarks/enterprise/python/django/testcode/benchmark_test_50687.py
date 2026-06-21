# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest50687(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    def _primary():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
