<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00298', methods: ['POST'])]
class BenchmarkTest00298Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
