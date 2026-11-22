<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00338Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $sessionCookie = cookie('session', (string)$userInput, 0, '/', null, false, true, false, 'strict');
        return response()->json(['ok' => 1])->withCookie($sessionCookie);
    }
}
