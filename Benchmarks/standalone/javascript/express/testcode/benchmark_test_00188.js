// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00188(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00188 };
