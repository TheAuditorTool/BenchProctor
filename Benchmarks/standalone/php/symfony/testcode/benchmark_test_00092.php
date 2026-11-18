<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00092', methods: ['POST'])]
class BenchmarkTest00092Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        [$data] = [$userInput, 'http'];
        $processed = (new \HTMLPurifier())->purify($data);
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
