<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00089Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $response = response()->json(['ok' => 1]);
        $response->header('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; HttpOnly; SameSite=Strict');
        return $response;
    }
}
