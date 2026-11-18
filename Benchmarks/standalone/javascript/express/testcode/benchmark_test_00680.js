// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00680(req, res) {
  const userInput = req.body.field || "";
  res.redirect(userInput);
}

module.exports = { BenchmarkTest00680 };
