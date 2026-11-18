// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00518(req, res) {
  const userInput = req.body || "";
  const data = userInput != null ? userInput : '';
  res.redirect(data);
}

module.exports = { BenchmarkTest00518 };
