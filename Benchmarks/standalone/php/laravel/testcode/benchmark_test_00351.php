<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00351Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = (!empty($userInput)) ? $userInput : '';
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
