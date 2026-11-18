// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00068(req, res) {
  const userInput = req.body.multipart_field || "";
  const [data] = String(userInput).split(',');
  res.redirect(data);
}

module.exports = { BenchmarkTest00068 };
