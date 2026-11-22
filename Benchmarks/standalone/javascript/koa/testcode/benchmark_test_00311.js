// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00311 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const { stringifySetCookie } = require("cookie");
  ctx.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(userInput), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00311 };
