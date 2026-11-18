// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00078(req, res) {
  const userInput = req.params.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00078 };
