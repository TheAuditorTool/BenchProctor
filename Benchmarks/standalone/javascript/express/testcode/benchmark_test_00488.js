// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00488(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = Buffer.from(userInput, "base64").toString();
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00488 };
