// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00348(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).replace(/\u0000/g, "");
  res.redirect(data);
}

module.exports = { BenchmarkTest00348 };
