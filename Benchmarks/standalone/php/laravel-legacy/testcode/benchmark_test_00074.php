<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00074Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = json_decode($userInput, true)['value'] ?? '';
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return response()->json(['ok' => 1]);
    }
}
