<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00158Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
