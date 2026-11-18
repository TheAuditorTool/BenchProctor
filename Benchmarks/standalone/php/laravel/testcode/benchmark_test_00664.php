<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00664Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
