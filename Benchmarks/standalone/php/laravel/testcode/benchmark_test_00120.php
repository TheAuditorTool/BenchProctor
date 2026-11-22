<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00120Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $tokenBytes = random_bytes(16);
        $token = bin2hex($tokenBytes);
        DB::statement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return response()->json(['reset' => 'sent'], 200);
    }
}
