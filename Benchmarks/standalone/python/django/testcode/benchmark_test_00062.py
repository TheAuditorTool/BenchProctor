# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00062(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
