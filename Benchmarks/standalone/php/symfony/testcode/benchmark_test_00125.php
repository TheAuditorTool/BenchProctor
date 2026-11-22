<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00125', methods: ['POST'])]
class BenchmarkTest00125Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = ($userInput !== null) ? $userInput : '';
        $quantity = (int) $data;
        $lineTotal = intval($quantity * 1999);
        return new JsonResponse(['line_total_cents' => $lineTotal], 200);
    }
}
