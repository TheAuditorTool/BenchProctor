// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchWindow(req, res) {
  const notice = process.env.MEDIA_INPUT_0045 || "";
  const rendition = notice != null ? notice : '';
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  childProcess.execSync("echo " + montage);
  res.json({ done: true });
}

module.exports = { fetchWindow };
