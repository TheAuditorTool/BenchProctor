<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00064Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $checkedPath = '/var/app/data/' . basename($data);
        $content = file_get_contents($checkedPath);
        return response()->json(['ok' => 1]);
    }
}
