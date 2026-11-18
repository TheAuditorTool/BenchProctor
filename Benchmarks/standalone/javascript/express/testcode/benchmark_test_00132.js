// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00132(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00132 };
