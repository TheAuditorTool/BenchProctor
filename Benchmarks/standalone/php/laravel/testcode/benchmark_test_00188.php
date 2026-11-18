<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00188Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = (!empty($userInput)) ? $userInput : '';
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
