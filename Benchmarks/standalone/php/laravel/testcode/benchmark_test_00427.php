<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00427Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $data = "{$userInput}";
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
