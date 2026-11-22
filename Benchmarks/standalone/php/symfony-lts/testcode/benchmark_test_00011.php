<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00011', methods: ['POST'])]
class BenchmarkTest00011Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = json_decode($userInput, true)['value'] ?? '';
        $processed = \Parsedown::instance()->setSafeMode(true)->text($data);
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
