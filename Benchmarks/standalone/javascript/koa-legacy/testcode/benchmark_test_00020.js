// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00020 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = userInput != null ? userInput : '';
  const { serialize } = require("cookie");
  ctx.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict" }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00020 };
