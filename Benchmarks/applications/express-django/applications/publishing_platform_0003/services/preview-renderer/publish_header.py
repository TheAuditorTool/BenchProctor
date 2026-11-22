# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def publish_header(request):
    heading = request.POST.get('field', '')
    if heading:
        addendum = heading
    else:
        addendum = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': addendum})))
