// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00314(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = userInput != null ? userInput : '';
  res.location(String(data)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00314 };
