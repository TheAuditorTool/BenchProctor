// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00136(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = nodeUtil.format("%s", userInput);
  const { serialize } = require("cookie");
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00136 };
