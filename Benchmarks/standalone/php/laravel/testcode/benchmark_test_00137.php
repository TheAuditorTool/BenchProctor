<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00137Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = json_decode($userInput, true)['value'] ?? '';
        $stream = function () use ($data) {
            echo '<div class="comment">' . $data . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
