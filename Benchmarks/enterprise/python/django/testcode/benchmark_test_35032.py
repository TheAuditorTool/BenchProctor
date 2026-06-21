# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest35032(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HttpResponse(Template(processed).render(Context()))
