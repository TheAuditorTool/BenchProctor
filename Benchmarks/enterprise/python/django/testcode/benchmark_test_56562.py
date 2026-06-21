# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest56562(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    def _primary():
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
