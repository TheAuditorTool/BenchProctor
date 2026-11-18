// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00460(req, res) {
  const userInput = req.body.multipart_field || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00460 };
