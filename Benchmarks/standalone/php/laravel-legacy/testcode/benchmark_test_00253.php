<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00253Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        \Illuminate\Support\Facades\Session::put(['data' => (string) $data, 'data_updated_at' => time()]);
        return response()->json(['ok' => 1]);
    }
}
