<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00207Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $sessionCookie = cookie('session', (string)$data, 0, '/', null, true, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
