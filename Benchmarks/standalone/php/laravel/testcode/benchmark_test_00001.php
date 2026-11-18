<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00001Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        file_put_contents('/var/uploads/' . $data, 'data');
        return response()->json(['ok' => 1]);
    }
}
