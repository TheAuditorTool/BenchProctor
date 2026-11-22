<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00153', methods: ['POST'])]
class BenchmarkTest00153Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $twig = new \Twig\Environment(new \Twig\Loader\ArrayLoader(['comment.html.twig' => '<div class="comment">{{ comment|raw }}</div>']));
        $html = $twig->render('comment.html.twig', ['comment' => $data]);
        return new Response($html, 200, ['Content-Type' => 'text/html']);
    }
}
