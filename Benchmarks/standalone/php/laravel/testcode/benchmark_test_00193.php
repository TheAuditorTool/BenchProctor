<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00193Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return response()->json(['ok' => 1]);
    }
}
