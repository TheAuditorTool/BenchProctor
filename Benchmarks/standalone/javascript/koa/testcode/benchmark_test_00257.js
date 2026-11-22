// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00257 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const { stringifySetCookie } = require("cookie");
  ctx.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00257 };
