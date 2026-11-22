// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const formatReceipt = async (req: Request, res: Response): Promise<void> => {
  const transcript = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(transcript);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + consignment + "</section>"); return;
}
