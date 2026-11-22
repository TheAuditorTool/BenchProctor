<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00061', methods: ['POST'])]
class BenchmarkTest00061Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $data = hex2bin($userInput);
        $hashCtx = hash_init('sha256');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return new JsonResponse(["committed" => true]);
    }
}
