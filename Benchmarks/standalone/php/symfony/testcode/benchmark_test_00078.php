<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00078', methods: ['POST'])]
class BenchmarkTest00078Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        return new RedirectResponse($data);
    }
}
