<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00010', methods: ['POST'])]
class BenchmarkTest00010Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        return new RedirectResponse($data);
    }
}
