<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00171', methods: ['POST'])]
class BenchmarkTest00171Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $_coerced = in_array(strtolower((string)$userInput), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$parsedBool], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return new JsonResponse(["committed" => true]);
    }
}
