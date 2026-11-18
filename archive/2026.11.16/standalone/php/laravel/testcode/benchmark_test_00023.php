<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00023Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $data = vsprintf('%1$s', [$userInput]);
        (new \Symfony\Component\Yaml\Parser())->parse($data, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return response()->json(['ok' => 1]);
    }
}
