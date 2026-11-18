// SPDX-License-Identifier: Apache-2.0

async function resolveSurvey(req, res) {
  const note = (await require("./shared").mq.receive("app-events"));
  let inquiry;
  try { inquiry = JSON.parse(note).value || ""; }
  catch (e) { inquiry = String(note); }
  JSON.parse(inquiry);
  res.json({ done: true });
}

module.exports = { resolveSurvey };
