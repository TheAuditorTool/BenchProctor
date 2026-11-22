// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00006(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  Object.assign(req.session, { data: String(data), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00006 };
