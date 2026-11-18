<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00075', methods: ['POST'])]
class BenchmarkTest00075Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $data = str_replace("\0", '', $userInput);
        return new Response('<div>' . $data . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
