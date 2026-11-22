<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00139', methods: ['POST'])]
class BenchmarkTest00139Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        [$data] = [$userInput, 'http'];
        $twig = new \Twig\Environment(new \Twig\Loader\ArrayLoader(['comment.html.twig' => '<div class="comment">{{ comment }}</div>']));
        $html = $twig->render('comment.html.twig', ['comment' => $data]);
        return new Response($html, 200, ['Content-Type' => 'text/html']);
    }
}
