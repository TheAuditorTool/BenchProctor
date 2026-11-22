// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00250(req, res) {
  const userInput = req.query.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const { stringifySetCookie } = require("cookie");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00250 };
