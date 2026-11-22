// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00244 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00244 };
