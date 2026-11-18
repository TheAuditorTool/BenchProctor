<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00508Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return response()->json(['token' => (string)$token], 200);
    }
}
