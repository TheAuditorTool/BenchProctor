// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchRecord(req, res) {
  const preface = process.env.MESSAGING_INPUT_0040 || "";
  const bulletin = preface != null ? preface : '';
  if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { res.status(400).json({error:"invalid"}); return; }
  const notice = bulletin;
  childProcess.execSync("echo " + notice);
  res.json({ done: true });
}

module.exports = { fetchRecord };
