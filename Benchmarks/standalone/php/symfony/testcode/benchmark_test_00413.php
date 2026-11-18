<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00413', methods: ['POST'])]
class BenchmarkTest00413Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
