// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

const BenchmarkTest00614 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + processed + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00614 };
