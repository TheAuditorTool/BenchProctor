<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00241', methods: ['POST'])]
class BenchmarkTest00241Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $stream = function () use ($data) {
            echo '<div class="comment">' . $data . '</div>';
        };
        return new \Symfony\Component\HttpFoundation\StreamedResponse($stream, 200, ['Content-Type' => 'text/html']);
    }
}
