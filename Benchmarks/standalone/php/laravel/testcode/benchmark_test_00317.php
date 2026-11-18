<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00317Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
