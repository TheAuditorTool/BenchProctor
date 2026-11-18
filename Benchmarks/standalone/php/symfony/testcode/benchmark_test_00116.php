<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00116', methods: ['POST'])]
class BenchmarkTest00116Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_search($ldap, 'ou=people,dc=example,dc=com', '(uid=' . $processed . ')');
        return new JsonResponse(["committed" => true]);
    }
}
