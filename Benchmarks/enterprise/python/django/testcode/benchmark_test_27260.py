# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest27260(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    processed = data[:64]
    return HttpResponse(Template(processed).render(Context()))
