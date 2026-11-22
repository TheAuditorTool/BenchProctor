<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00249Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $stream = function () use ($data) {
            echo '<div class="comment">' . e($data) . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
