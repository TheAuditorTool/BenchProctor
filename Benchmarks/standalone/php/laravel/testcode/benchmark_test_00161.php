<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00161Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1')->body;
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        (new \Symfony\Component\Yaml\Parser())->parse($data, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return response()->json(['ok' => 1]);
    }
}
