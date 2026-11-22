// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizeReceipt(req, res) {
  const citation = req.headers.referer || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const rendition = normalize(citation);
  childProcess.exec("echo " + rendition, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { normalizeReceipt };
