// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00036(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00036 };
