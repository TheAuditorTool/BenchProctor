// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const archiveRecord = async (req: Request, res: Response): Promise<void> => {
  const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = remark;
  const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send("<div>" + remittance + "</div>");
}
