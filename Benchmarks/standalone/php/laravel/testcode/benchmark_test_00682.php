<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00682Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return response()->json(['token' => (string)$token], 200);
    }
}
