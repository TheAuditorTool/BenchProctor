// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

async function BenchmarkTest00216(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = userInput != null ? userInput : '';
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  const password = String(req.body?.password ?? "");
  if (!password) { res.status(400).json({ error: "password required" }); return; }
  const authenticated = await new Promise((resolve) => {
    ldapClient.bind("uid=" + data + ",ou=people,dc=example,dc=com", password, (err) => { ldapClient.unbind(); resolve(!err); });
  });
  res.json({ authenticated }); return;
}

module.exports = { BenchmarkTest00216 };
