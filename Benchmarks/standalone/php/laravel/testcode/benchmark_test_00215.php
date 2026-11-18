<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00215Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
