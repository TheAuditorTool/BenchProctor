// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00280(req, res) {
  const userInput = req.headers.authorization || "";
  const [data] = String(userInput).split(',');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00280 };
