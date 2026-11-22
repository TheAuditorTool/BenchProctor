<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00136Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $stream = function () use ($data) {
            echo '<div class="comment">' . $data . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
