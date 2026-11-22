// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00347(req, res) {
  const userInput = req.body?.field || "";
  const data = String(userInput).slice(0, 200);
  const { stringifySetCookie } = require("cookie");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00347 };
