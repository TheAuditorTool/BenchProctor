// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00251(req, res) {
  const userInput = req.headers.origin || "";
  const data = `${userInput}`;
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00251 };
