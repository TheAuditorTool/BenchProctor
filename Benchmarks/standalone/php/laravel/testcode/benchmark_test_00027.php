<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00027Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $processed = (new \HTMLPurifier())->purify($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
