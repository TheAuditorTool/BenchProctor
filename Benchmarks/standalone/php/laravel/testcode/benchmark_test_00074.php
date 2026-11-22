<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00074Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = str_replace("\0", '', $userInput);
        ini_set('yaml.decode_php', '1');
        $document = yaml_parse((string)$data);
        return response()->json(['ok' => 1]);
    }
}
