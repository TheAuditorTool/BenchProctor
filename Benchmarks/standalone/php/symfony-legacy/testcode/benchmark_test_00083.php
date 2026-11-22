<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00083', methods: ['POST'])]
class BenchmarkTest00083Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = json_decode($userInput, true)['value'] ?? '';
        $processed = (new \HTMLPurifier())->purify($data);
        $stream = function () use ($processed) {
            echo '<div class="comment">' . $processed . '</div>';
        };
        return new \Symfony\Component\HttpFoundation\StreamedResponse($stream, 200, ['Content-Type' => 'text/html']);
    }
}
