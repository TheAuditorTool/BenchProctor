<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00252', methods: ['POST'])]
class BenchmarkTest00252Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = ($userInput !== null) ? $userInput : '';
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        $twig = new \Twig\Environment(new \Twig\Loader\ArrayLoader(['comment.html.twig' => '<div class="comment">{{ comment|raw }}</div>']));
        $html = $twig->render('comment.html.twig', ['comment' => $processed]);
        return new Response($html, 200, ['Content-Type' => 'text/html']);
    }
}
