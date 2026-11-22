// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00188(req, res) {
  const userInput = req.body.multipart_field || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  vm.runInNewContext(String(data), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00188 };
