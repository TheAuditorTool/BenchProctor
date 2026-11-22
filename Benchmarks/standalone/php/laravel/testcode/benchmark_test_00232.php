<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00232Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $_coerced = (float)$data;
        $processed = $_coerced;
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $processed);
        return response()->json(['ok' => 1]);
    }
}
