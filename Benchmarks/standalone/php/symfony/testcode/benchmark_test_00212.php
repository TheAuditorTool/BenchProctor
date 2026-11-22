<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00212', methods: ['POST'])]
class BenchmarkTest00212Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = ($userInput !== null) ? $userInput : '';
        $hashCtx = hash_init('md4');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return new JsonResponse(["committed" => true]);
    }
}
