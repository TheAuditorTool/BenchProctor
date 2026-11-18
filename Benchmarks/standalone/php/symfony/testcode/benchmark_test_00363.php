<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00363', methods: ['POST'])]
class BenchmarkTest00363Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        return new Response(htmlspecialchars((string)$data, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'), 200, ['Content-Type' => 'text/html']);
    }
}
