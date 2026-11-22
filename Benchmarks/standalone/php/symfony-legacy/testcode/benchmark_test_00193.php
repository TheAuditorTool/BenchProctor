<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00193', methods: ['POST'])]
class BenchmarkTest00193Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        [$data] = [$userInput, 'http'];
        $processed = (new \HTMLPurifier())->purify($data);
        $stream = function () use ($processed) {
            echo '<div class="comment">' . $processed . '</div>';
        };
        return new \Symfony\Component\HttpFoundation\StreamedResponse($stream, 200, ['Content-Type' => 'text/html']);
    }
}
