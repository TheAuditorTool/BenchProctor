// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00576(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const [data] = String(userInput).split(',');
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00576 };
