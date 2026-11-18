<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00681', methods: ['POST'])]
class BenchmarkTest00681Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
