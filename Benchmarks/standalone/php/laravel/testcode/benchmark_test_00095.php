<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00095Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = str_replace("\0", '', $userInput);
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
