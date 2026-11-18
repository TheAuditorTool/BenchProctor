<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00112Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        system('gzip -f /var/app/reports/' . (string)$allowedBin);
        return response()->json(['ok' => 1]);
    }
}
