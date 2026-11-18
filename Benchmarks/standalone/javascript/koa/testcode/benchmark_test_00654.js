// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00654 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00654 };
