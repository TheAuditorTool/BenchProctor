// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00004(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const [data] = String(userInput).split(',');
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00004 };
