// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const verifyReceipt = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body as string) || "";
  const rendition = Buffer.from(notice, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [rendition]);
  res.json({ accepted: true });
}
