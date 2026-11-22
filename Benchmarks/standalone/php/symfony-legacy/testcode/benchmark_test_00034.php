<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00034', methods: ['POST'])]
class BenchmarkTest00034Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = "{$userInput}";
        return new Response('', 302, ['Location' => (string)$data]);
    }
}
