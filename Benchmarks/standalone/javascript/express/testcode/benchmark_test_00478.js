// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00478(req, res) {
  const userInput = req.headers.referer || "";
  const data = decodeURIComponent(userInput);
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00478 };
