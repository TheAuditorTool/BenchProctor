# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest08691(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return HttpResponse(Template(data).render(Context()))
