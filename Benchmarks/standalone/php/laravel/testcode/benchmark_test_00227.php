<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00227Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        return \Illuminate\Support\Facades\Redirect::away((string)$userInput);
    }
}
