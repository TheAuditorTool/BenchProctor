<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00184Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $html = \Illuminate\Support\Facades\Blade::render('<div class="comment">{!! $comment !!}</div>', ['comment' => $data]);
        return response($html)->header('Content-Type', 'text/html');
    }
}
