<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00163', methods: ['POST'])]
class BenchmarkTest00163Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $response = new RedirectResponse('/account');
        $response->setTargetUrl((string)$data);
        return $response;
    }
}
