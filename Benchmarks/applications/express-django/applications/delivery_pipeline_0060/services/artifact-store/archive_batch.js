// SPDX-License-Identifier: Apache-2.0

async function archiveBatch(req, res) {
  const wording = req.body.field || "";
  const remark = decodeURIComponent(wording);
  res.send("<div>" + remark + "</div>");
}

module.exports = { archiveBatch };
