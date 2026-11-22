// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00033 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00033 };
