// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00186 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00186 };
