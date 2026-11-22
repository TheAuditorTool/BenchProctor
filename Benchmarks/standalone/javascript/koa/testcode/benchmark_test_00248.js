// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00248 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const { stringifySetCookie } = require("cookie");
  ctx.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00248 };
