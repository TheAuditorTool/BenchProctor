<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00195', methods: ['POST'])]
class BenchmarkTest00195Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $hashCtx = hash_init('md4');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return new JsonResponse(["committed" => true]);
    }
}
