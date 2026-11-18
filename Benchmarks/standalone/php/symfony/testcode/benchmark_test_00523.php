<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00523', methods: ['POST'])]
class BenchmarkTest00523Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        return new RedirectResponse($userInput);
    }
}
