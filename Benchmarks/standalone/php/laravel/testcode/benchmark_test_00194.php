<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00194Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return response()->json(['token' => (string)$token], 200);
    }
}
