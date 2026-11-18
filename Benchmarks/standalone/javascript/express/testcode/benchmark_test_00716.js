// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00716(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00716 };
