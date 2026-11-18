<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00146', methods: ['POST'])]
class BenchmarkTest00146Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
