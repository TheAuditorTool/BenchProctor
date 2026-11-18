<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00608Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        eval((string)$parsedBool);
        return response()->json(['ok' => 1]);
    }
}
