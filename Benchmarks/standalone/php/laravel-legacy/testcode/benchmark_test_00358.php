<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00358Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
