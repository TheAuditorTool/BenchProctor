// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00320(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = `${userInput}`;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00320 };
