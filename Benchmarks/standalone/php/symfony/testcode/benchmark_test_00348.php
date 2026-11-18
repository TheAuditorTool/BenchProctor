<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00348', methods: ['POST'])]
class BenchmarkTest00348Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = json_decode($userInput, true)['value'] ?? '';
        return new Response('<div>' . $data . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
