<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00131', methods: ['POST'])]
class BenchmarkTest00131Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = vsprintf('%1$s', [$userInput]);
        $hashCtx = hash_init('sha256');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return new JsonResponse(["committed" => true]);
    }
}
