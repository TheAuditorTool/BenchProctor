// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00061(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = nodeUtil.format("%s", userInput);
  res.location(String(data)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00061 };
