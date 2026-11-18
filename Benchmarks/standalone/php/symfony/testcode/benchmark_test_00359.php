<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00359', methods: ['POST'])]
class BenchmarkTest00359Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = (!empty($userInput)) ? $userInput : '';
        return new RedirectResponse($data);
    }
}
