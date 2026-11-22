<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00295Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
