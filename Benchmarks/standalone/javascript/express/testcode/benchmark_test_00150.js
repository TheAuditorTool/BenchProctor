// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00150(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const { stringifySetCookie } = require("cookie");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00150 };
