<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00459Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = vsprintf('%1$s', [$userInput]);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
