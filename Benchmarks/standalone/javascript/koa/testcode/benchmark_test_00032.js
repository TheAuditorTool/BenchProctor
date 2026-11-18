// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

const BenchmarkTest00032 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(userInput)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = userInput;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + processed + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00032 };
