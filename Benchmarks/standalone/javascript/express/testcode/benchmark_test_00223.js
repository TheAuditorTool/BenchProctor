// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00223(req, res) {
  const userInput = req.body || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00223 };
