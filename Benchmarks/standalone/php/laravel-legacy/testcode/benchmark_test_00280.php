<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00280Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return response()->json(['wrapped' => $wrapped], 200);
    }
}
