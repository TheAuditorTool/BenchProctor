<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00412Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return response()->json(['wrapped' => $wrapped], 200);
    }
}
