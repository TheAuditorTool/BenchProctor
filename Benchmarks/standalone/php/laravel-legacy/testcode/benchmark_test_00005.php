<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00005Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $html = \Illuminate\Support\Facades\Blade::render('<div class="comment">{!! $comment !!}</div>', ['comment' => $userInput]);
        return response($html)->header('Content-Type', 'text/html');
    }
}
