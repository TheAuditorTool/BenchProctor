// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const exportPolicy = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const grievance = Buffer.from(summary, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [grievance]);
  res.json({ accepted: true });
}
