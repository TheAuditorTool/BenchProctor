<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00085', methods: ['POST'])]
class BenchmarkTest00085Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        unserialize($data);
        return new JsonResponse(["committed" => true]);
    }
}
