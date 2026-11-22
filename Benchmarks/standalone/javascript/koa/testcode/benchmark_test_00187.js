// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

const BenchmarkTest00187 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = userInput != null ? userInput : '';
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  const password = String((ctx.request.body && ctx.request.body.password) || "");
  if (!password) { ctx.status = 400; ctx.body = { error: "password required" }; return; }
  const authenticated = await new Promise((resolve) => {
    ldapClient.bind("uid=" + data + ",ou=people,dc=example,dc=com", password, (err) => { ldapClient.unbind(); resolve(!err); });
  });
  ctx.body = { authenticated }; return;
}

module.exports = { BenchmarkTest00187 };
