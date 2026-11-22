// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00260(req, res) {
  const userInput = req.body.multipart_field || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00260 };
