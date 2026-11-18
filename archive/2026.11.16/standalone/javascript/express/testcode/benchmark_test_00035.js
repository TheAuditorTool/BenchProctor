// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00035(req, res) {
  const userInput = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00035 };
