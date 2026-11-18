// SPDX-License-Identifier: Apache-2.0

async function publishCheckpoint(req, res) {
  const footnote = (await require("./shared").mq.receive("app-events"));
  let wording;
  try { wording = JSON.parse(footnote).value || ""; }
  catch (e) { wording = String(footnote); }
  JSON.parse(wording);
  res.json({ done: true });
}

module.exports = { publishCheckpoint };
