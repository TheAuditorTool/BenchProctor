<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00249Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $html = \Illuminate\Support\Facades\Blade::render('<div class="comment">{!! $comment !!}</div>', ['comment' => $data]);
        return response($html)->header('Content-Type', 'text/html');
    }
}
