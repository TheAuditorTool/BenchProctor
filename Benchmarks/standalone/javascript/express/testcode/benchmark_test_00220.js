// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00220(req, res) {
  const userInput = req.headers.authorization || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const { stringifySetCookie } = require("cookie");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00220 };
