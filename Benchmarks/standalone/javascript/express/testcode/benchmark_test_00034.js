// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00034(req, res) {
  const userInput = req.cookies.session_token || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00034 };
