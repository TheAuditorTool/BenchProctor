// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const enrichBundle = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body as string) || "";
  const inquiry = Buffer.from(note, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [inquiry]);
  res.json({ accepted: true });
}
