<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00471', methods: ['POST'])]
class BenchmarkTest00471Controller
{
    public function __invoke()
    {
        $token = bin2hex(random_bytes(32));
        return new JsonResponse(['token' => (string)$token], 200);
    }
}
