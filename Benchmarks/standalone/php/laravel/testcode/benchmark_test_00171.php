<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00171Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
