<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00588Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $data = (!empty($userInput)) ? $userInput : '';
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
