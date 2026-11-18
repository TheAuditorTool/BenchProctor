<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00121Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $data = json_decode($userInput, true)['value'] ?? '';
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return response()->json(['wrapped' => $wrapped], 200);
    }
}
