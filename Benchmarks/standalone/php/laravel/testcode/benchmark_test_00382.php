<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00382Controller
{
    public function __invoke()
    {
        $userInput = config('app.value', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        \App\Models\User::where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
