<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00440', methods: ['POST'])]
class BenchmarkTest00440Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        return new RedirectResponse($data);
    }
}
