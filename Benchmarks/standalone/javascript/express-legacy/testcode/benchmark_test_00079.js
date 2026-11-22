// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00079(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = decodeURIComponent(userInput);
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00079 };
