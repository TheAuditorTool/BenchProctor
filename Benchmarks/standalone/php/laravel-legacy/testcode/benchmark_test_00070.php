<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00070Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = json_decode($userInput, true)['value'] ?? '';
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        $stream = function () use ($processed) {
            echo '<div class="comment">' . $processed . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
