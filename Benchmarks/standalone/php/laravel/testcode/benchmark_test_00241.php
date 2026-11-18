<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00241Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
