<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00143', methods: ['POST'])]
class BenchmarkTest00143Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        return new RedirectResponse($userInput);
    }
}
