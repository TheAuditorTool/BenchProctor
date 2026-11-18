<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00300', methods: ['POST'])]
class BenchmarkTest00300Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return new JsonResponse(["committed" => true]);
    }
}
