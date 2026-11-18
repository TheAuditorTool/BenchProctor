// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00004(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const [data] = String(userInput).split(',');
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00004 };
