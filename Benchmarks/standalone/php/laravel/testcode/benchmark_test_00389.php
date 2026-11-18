<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00389Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_search($ldap, 'ou=people,dc=example,dc=com', '(uid=' . $data . ')');
        return response()->json(['ok' => 1]);
    }
}
