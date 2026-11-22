// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00091(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const token = String(userInput).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00091 };
