// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00001(req, res) {
  const userInput = req.body.multipart_field || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00001 };
