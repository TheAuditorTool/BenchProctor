// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00351(req, res) {
  const userInput = req.headers.authorization || "";
  const data = userInput != null ? userInput : '';
  res.redirect(data);
}

module.exports = { BenchmarkTest00351 };
