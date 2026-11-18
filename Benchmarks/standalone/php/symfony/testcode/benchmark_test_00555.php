<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00555', methods: ['POST'])]
class BenchmarkTest00555Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        return new RedirectResponse($data);
    }
}
