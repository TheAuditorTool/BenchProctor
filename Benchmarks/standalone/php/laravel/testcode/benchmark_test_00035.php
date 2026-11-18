<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00035Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
