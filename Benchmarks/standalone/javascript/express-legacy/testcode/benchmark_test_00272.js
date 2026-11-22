// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00272(req, res) {
  const userInput = req.headers.referer || "";
  const data = `${userInput}`;
  const { serialize } = require("cookie");
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00272 };
