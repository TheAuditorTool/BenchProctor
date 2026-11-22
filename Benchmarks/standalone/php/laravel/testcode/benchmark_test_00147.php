<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00147Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $content = file_get_contents('/var/app/data/' . (string)$userInput);
        return response()->json(['ok' => 1]);
    }
}
