// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00314(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.redirect(data);
}

module.exports = { BenchmarkTest00314 };
