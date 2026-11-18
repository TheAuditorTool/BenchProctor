// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00470(req, res) {
  const userInput = req.params.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.redirect(data);
}

module.exports = { BenchmarkTest00470 };
