// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

async function BenchmarkTest00322(req, res) {
  const userInput = req.headers.host || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + data + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00322 };
