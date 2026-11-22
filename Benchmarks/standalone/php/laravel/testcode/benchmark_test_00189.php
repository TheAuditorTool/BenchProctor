<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00189Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = sprintf('%s', $userInput);
        return response(e($data))->header('Content-Type', 'text/html');
    }
}
