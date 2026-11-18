// SPDX-License-Identifier: Apache-2.0

async function archiveSchedule(req, res) {
  const remark = (await require("./shared").mq.receive("app-events"));
  let remittance;
  try { remittance = JSON.parse(remark).value || ""; }
  catch (e) { remittance = String(remark); }
  JSON.parse(remittance);
  res.json({ done: true });
}

module.exports = { archiveSchedule };
