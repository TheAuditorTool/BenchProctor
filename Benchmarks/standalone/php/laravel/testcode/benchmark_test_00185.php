<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00185Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
