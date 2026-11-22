<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00224Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return response()->json(['ok' => 1]);
    }
}
