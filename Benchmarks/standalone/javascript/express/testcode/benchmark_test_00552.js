// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00552(req, res) {
  const userInput = req.headers.referer || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00552 };
