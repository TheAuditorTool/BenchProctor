<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00193Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $sessionCookie = cookie('session', (string)$data, 0, '/', null, false, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
