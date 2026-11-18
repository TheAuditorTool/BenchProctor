<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00112', methods: ['POST'])]
class BenchmarkTest00112Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        unserialize($data);
        return new JsonResponse(["committed" => true]);
    }
}
