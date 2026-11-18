// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const collectReport = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body as string) || "";
  const cohort = Buffer.from(headline, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [cohort]);
  res.json({ accepted: true });
}
