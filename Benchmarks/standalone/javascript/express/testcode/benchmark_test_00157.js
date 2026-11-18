// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00157(req, res) {
  const userInput = req.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00157 };
