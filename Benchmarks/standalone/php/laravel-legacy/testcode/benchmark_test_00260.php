<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00260Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = str_replace("\0", '', $userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        session(['data' => (string) $processed]);
        return response()->json(['ok' => 1]);
    }
}
