<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00204Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = "{$userInput}";
        (new \Symfony\Component\Yaml\Parser())->parse($data, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return response()->json(['ok' => 1]);
    }
}
