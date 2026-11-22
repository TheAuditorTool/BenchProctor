// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00190 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + processed + "']").select({ node: usersDoc });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00190 };
