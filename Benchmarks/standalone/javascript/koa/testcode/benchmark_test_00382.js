// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00382 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00382 };
