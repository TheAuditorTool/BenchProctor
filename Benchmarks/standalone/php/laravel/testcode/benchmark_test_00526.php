<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00526Controller
{
    public function __invoke()
    {
        $token = bin2hex(random_bytes(32));
        return response()->json(['token' => (string)$token], 200);
    }
}
