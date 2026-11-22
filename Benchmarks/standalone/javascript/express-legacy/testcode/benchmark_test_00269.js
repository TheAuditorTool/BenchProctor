// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00269(req, res) {
  const userInput = req.headers.authorization || "";
  const [data] = String(userInput).split(',');
  new Function("return (" + String(data) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00269 };
