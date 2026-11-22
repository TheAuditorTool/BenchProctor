// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00350(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  Object.assign(req.session, { data: String(userInput), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00350 };
