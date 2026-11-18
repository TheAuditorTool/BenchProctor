// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00673 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00673 };
