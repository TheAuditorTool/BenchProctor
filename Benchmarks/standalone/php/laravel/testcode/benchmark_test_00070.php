<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00070Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = (!empty($userInput)) ? $userInput : '';
        $html = \Illuminate\Support\Facades\Blade::render('<div class="comment">{{ $comment }}</div>', ['comment' => $data]);
        return response($html)->header('Content-Type', 'text/html');
    }
}
