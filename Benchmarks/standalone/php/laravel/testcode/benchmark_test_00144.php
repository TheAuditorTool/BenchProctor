<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00144Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return redirect($targetUrl);
    }
}
