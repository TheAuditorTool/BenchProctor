// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00073(req, res) {
  const userInput = req.body.multipart_field || "";
  const [data] = String(userInput).split(',');
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00073 };
