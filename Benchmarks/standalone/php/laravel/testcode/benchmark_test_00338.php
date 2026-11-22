<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00338Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $sessionCookie = cookie('session', (string)$data, 0, '/', null, false, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
