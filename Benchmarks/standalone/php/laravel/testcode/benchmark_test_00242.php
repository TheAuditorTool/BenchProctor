<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00242Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = hex2bin($userInput);
        $errno = 0; $errstr = '';
        fsockopen((string) parse_url((string)$data, PHP_URL_HOST), 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
