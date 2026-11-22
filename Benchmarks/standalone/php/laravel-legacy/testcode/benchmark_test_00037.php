<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00037Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $_coerced = (float)$data;
        $processed = $_coerced;
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $processed);
        return response()->json(['ok' => 1]);
    }
}
