<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00141Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $data = str_replace("\0", '', $userInput);
        $sessionCookie = cookie('session', (string)$data, 0, '/', null, true, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
