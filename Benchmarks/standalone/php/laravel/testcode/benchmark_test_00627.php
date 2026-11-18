<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00627Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('/tmp/data');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        \App\Models\User::where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
