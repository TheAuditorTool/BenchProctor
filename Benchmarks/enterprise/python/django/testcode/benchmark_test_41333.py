# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest41333(request):
    upload_name = request.FILES['upload'].name
    data = default_blank(upload_name)
    processed = data[:64]
    return HttpResponse(Template(processed).render(Context()))
