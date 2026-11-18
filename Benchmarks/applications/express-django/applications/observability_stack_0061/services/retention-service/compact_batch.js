// SPDX-License-Identifier: Apache-2.0

async function compactBatch(req, res) {
  const headline = (await require("./shared").mq.receive("app-events"));
  let cohort;
  try { cohort = JSON.parse(headline).value || ""; }
  catch (e) { cohort = String(headline); }
  JSON.parse(cohort);
  res.json({ done: true });
}

module.exports = { compactBatch };
