# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import requests


def BenchmarkTest00150(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    return redirect(str(api_value))
