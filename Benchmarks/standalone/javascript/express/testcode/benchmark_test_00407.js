// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

async function BenchmarkTest00407(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(userInput)) { res.status(400).json({error:"invalid"}); return; }
  const processed = userInput;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + processed + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00407 };
