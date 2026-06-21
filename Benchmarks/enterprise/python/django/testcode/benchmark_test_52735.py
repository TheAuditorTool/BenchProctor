# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest52735(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    return HttpResponse(Template(data).render(Context()))
