<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00307Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
