<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00089Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $data = sprintf('%s', $userInput);
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
