// SPDX-License-Identifier: Apache-2.0

async function validatePolicy(req, res) {
  const subject = (await require("./shared").mq.receive("app-events"));
  let bulletin;
  try { bulletin = JSON.parse(subject).value || ""; }
  catch (e) { bulletin = String(subject); }
  JSON.parse(bulletin);
  res.json({ done: true });
}

module.exports = { validatePolicy };
