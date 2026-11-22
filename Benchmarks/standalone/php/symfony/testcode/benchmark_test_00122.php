<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00122', methods: ['POST'])]
class BenchmarkTest00122Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_list($ldap, 'ou=people,dc=example,dc=com', '(mail=' . $processed . ')', ['uid', 'cn']);
        return new JsonResponse(["committed" => true]);
    }
}
