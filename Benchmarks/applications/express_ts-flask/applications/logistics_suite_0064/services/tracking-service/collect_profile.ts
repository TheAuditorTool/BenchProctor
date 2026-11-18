// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const collectProfile = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body as string) || "";
  const parcel = Buffer.from(transcript, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [parcel]);
  res.json({ accepted: true });
}
