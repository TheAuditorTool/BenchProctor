<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00268Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = hex2bin($userInput);
        $stream = function () use ($data) {
            echo '<div class="comment">' . $data . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
