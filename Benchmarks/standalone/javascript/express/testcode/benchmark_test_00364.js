// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00364(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00364 };
