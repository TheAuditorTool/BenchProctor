// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00096(req, res) {
  const userInput = req.body.multipart_field || "";
  eval(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00096 };
