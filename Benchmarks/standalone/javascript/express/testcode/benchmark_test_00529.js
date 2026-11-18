// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00529(req, res) {
  const userInput = req.query.id || "";
  const data = decodeURIComponent(userInput);
  res.redirect(data);
}

module.exports = { BenchmarkTest00529 };
