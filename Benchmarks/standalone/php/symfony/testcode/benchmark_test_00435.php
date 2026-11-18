<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00435', methods: ['POST'])]
class BenchmarkTest00435Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        return new Response('<div>' . $data . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
