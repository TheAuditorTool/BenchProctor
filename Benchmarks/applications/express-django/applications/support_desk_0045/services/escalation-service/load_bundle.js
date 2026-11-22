// SPDX-License-Identifier: Apache-2.0

async function loadBundle(req, res) {
  const remark = req.body?.payload || "";
  const inquiry = `${remark}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + inquiry + "</section>"); return;
}

module.exports = { loadBundle };
