<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00237Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        unlink('/var/app/data/' . $data);
        return response()->json(['ok' => 1]);
    }
}
