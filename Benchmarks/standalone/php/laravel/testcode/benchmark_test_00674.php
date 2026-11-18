<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00674Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
