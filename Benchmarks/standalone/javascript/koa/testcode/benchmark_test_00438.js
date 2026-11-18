// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00438 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00438 };
