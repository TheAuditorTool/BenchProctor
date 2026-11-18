// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00690(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00690 };
