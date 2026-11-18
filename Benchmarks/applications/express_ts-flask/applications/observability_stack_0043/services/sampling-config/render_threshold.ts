// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const renderThreshold = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body as string) || "";
  const gauge = Buffer.from(note, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [gauge]);
  res.json({ accepted: true });
}
