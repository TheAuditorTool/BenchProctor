// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00111(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00111 };
