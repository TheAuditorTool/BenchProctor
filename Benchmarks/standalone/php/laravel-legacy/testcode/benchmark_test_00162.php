<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00162Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $response = response()->json(['ok' => 1]);
        $response->header('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; Secure; HttpOnly; SameSite=Strict');
        return $response;
    }
}
