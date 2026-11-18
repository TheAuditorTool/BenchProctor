<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00089Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = vsprintf('%1$s', [$userInput]);
        system('gzip -f /var/app/reports/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
