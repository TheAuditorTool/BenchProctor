<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00027', methods: ['POST'])]
class BenchmarkTest00027Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = base64_decode($userInput);
        $twig = new \Twig\Environment(new \Twig\Loader\ArrayLoader(['comment.html.twig' => '<div class="comment">{{ comment|raw }}</div>']));
        $html = $twig->render('comment.html.twig', ['comment' => $data]);
        return new Response($html, 200, ['Content-Type' => 'text/html']);
    }
}
