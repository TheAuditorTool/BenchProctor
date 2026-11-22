// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00360(req, res) {
  const userInput = req.body.field || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const { serialize } = require("cookie");
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00360 };
