// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00232(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  req.app.locals.announcement = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00232 };
