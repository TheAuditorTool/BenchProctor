// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00006(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).slice(0, 200);
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00006 };
