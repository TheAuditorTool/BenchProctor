<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00078', methods: ['POST'])]
class BenchmarkTest00078Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
