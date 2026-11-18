// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00127(req, res) {
  const userInput = req.query.id || "";
  const data = Buffer.from(userInput, "hex").toString();
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00127 };
