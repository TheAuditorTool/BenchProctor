// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00136(req, res) {
  const userInput = req.headers.authorization || "";
  const { stringifySetCookie } = require("cookie");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(userInput), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00136 };
