// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00044(req, res) {
  const userInput = req.body.field || "";
  const token = String(userInput).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00044 };
