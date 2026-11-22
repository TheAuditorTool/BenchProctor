<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00102Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        [$data] = [$userInput, 'http'];
        $sessionCookie = cookie('session', (string)$data, 0, '/', null, false, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
