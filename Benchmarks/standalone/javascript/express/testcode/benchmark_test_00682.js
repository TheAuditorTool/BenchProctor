// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00682(req, res) {
  const userInput = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00682 };
