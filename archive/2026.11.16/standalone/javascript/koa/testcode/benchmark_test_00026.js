// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00026 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00026 };
