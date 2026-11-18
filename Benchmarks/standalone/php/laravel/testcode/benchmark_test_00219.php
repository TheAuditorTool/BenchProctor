<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00219Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        [$data] = [$userInput, 'http'];
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return response()->json(['wrapped' => $wrapped], 200);
    }
}
