<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00034', methods: ['POST'])]
class BenchmarkTest00034Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $hashCtx = hash_init('md4');
        hash_update($hashCtx, (string)$userInput);
        $digest = hash_final($hashCtx);
        return new JsonResponse(["committed" => true]);
    }
}
