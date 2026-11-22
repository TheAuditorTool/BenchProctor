# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00105(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
