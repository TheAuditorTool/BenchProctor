// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00604(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = String(userInput).slice(0, 200);
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00604 };
