// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00032(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00032 };
