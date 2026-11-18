// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00456 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = Buffer.from(userInput, "base64").toString();
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00456 };
