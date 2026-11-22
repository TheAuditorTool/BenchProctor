<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00159', methods: ['POST'])]
class BenchmarkTest00159Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $quantity = (int) $data;
        $lineTotal = intval($quantity * 1999);
        return new JsonResponse(['line_total_cents' => $lineTotal], 200);
    }
}
