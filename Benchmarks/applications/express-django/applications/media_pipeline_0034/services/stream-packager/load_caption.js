// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function loadCaption(req, res) {
  const synopsis = req.cookies.session_token || "";
  const rendition = decodeURIComponent(synopsis);
  childProcess.spawn("echo " + rendition, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { loadCaption };
