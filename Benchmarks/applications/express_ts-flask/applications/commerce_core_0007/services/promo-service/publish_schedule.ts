// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const publishSchedule = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body as string) || "";
  const voucher = Buffer.from(heading, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [voucher]);
  res.json({ accepted: true });
}
