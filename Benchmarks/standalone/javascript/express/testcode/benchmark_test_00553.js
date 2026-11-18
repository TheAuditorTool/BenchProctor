// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00553(req, res) {
  const userInput = req.headers.host || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00553 };
