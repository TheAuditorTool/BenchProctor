// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const publishQuota = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body as string) || "";
  const persona = Buffer.from(passage, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [persona]);
  res.json({ accepted: true });
}
