<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00340Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $sessionCookie = cookie('session', (string)$data, 0, '/', null, true, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
