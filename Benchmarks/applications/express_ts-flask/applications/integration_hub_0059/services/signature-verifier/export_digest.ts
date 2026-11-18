// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const exportDigest = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body as string) || "";
  const handshake = Buffer.from(synopsis, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [handshake]);
  res.json({ accepted: true });
}
