// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00444(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = `${userInput}`;
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00444 };
