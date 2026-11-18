<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00683Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        unlink('/var/app/data/' . $data);
        return response()->json(['ok' => 1]);
    }
}
