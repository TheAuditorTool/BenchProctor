// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00185(req, res) {
  const userInput = req.query.id || "";
  const data = Buffer.from(userInput, "hex").toString();
  res.location(String(data)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00185 };
