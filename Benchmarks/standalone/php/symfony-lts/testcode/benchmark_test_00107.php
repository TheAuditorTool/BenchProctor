<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00107', methods: ['POST'])]
class BenchmarkTest00107Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $data = "{$userInput}";
        $quantity = (int) $data;
        $lineTotal = intval($quantity * 1999);
        return new JsonResponse(['line_total_cents' => $lineTotal], 200);
    }
}
