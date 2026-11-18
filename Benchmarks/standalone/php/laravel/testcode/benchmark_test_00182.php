<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00182Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = ($userInput !== null) ? $userInput : '';
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
