// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const collectFulfillment = async (req: Request, res: Response): Promise<void> => {
  const notice = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = notice;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(backorder))) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
  res.send(fileContent);
}
