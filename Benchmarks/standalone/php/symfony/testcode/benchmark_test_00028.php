<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00028', methods: ['POST'])]
class BenchmarkTest00028Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $data = vsprintf('%1$s', [$userInput]);
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return new JsonResponse(['token' => (string)$token], 200);
    }
}
