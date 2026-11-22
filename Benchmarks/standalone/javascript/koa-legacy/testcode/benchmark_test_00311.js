// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00311 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = nodeUtil.format("%s", userInput);
  const { serialize } = require("cookie");
  ctx.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00311 };
