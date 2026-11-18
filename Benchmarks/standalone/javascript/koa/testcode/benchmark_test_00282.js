// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00282 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00282 };
