// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00101(req, res) {
  const userInput = req.headers.referer || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00101 };
