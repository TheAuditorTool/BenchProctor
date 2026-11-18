<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00092Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = urldecode($userInput);
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        session(['data' => (string) $parsedBool]);
        return response()->json(['ok' => 1]);
    }
}
