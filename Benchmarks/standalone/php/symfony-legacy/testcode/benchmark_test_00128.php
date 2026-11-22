<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00128', methods: ['POST'])]
class BenchmarkTest00128Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $response = new RedirectResponse('/account');
        $response->setTargetUrl((string)$data);
        return $response;
    }
}
