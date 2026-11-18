<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00540Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = base64_decode($userInput);
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
