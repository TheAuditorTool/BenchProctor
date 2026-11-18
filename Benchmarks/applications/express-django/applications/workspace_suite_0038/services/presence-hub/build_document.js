// SPDX-License-Identifier: Apache-2.0

async function buildDocument(req, res) {
  const preface = (await require("./shared").mq.receive("app-events"));
  let remark;
  try { remark = JSON.parse(preface).value || ""; }
  catch (e) { remark = String(preface); }
  JSON.parse(remark);
  res.json({ done: true });
}

module.exports = { buildDocument };
