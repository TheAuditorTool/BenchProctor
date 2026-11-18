// SPDX-License-Identifier: Apache-2.0

async function archiveReport(req, res) {
  const subject = (await require("./shared").mq.receive("app-events"));
  let ledger;
  try { ledger = JSON.parse(subject).value || ""; }
  catch (e) { ledger = String(subject); }
  JSON.parse(ledger);
  res.json({ done: true });
}

module.exports = { archiveReport };
