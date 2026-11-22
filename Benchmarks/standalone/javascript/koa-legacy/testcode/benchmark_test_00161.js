// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00161 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const { serialize } = require("cookie");
  ctx.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict" }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00161 };
