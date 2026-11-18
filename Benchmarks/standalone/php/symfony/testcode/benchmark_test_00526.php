<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00526', methods: ['POST'])]
class BenchmarkTest00526Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $data = ($userInput !== null) ? $userInput : '';
        return new RedirectResponse($data);
    }
}
