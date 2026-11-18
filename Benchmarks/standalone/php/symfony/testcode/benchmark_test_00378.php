<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00378', methods: ['POST'])]
class BenchmarkTest00378Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
