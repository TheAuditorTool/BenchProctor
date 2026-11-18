// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00110(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const [data] = String(userInput).split(',');
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00110 };
