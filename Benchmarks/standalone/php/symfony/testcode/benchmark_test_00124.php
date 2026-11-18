<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00124', methods: ['POST'])]
class BenchmarkTest00124Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        return new Response('<div>' . $userInput . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
