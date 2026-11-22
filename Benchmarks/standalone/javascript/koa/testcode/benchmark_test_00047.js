// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00047 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).slice(0, 200);
  const { stringifySetCookie } = require("cookie");
  ctx.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00047 };
