// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00658(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.redirect(data);
}

module.exports = { BenchmarkTest00658 };
