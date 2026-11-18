<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00629Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        (new \Symfony\Component\Yaml\Parser())->parse($userInput, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return response()->json(['ok' => 1]);
    }
}
