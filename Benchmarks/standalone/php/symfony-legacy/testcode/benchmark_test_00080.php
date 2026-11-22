<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00080', methods: ['POST'])]
class BenchmarkTest00080Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $digestBytes = sodium_crypto_generichash((string)$userInput);
        $digest = sodium_bin2hex($digestBytes);
        return new JsonResponse(["committed" => true]);
    }
}
