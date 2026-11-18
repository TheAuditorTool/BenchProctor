<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00084Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
