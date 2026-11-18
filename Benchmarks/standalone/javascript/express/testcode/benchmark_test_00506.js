// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00506(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00506 };
