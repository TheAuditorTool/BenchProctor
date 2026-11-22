<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00340Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $response = response()->json(['ok' => 1]);
        $response->header('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; Secure; HttpOnly; SameSite=Strict');
        return $response;
    }
}
