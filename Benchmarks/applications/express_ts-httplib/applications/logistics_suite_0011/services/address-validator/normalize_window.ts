// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const normalizeWindow = async (req: Request, res: Response): Promise<void> => {
  const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = citation;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(consignment))) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
  res.send(fileContent);
}
