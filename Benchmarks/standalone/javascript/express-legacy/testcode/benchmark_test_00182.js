// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00182(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const { serialize } = require("cookie");
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00182 };
