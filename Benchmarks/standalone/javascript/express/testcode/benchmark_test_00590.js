// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00590(req, res) {
  const userInput = req.params.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00590 };
