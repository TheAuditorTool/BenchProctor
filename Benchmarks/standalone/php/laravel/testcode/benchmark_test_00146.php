<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00146Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
