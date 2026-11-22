<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00025Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $rng = new \Random\Randomizer(new \Random\Engine\Mt19937());
        $token = bin2hex($rng->getBytes(16));
        DB::statement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return response()->json(['reset' => 'sent'], 200);
    }
}
