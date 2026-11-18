// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00454(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00454 };
