<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00055Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $data = base64_decode($userInput);
        (new \Symfony\Component\Yaml\Parser())->parse($data, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return response()->json(['ok' => 1]);
    }
}
