// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const enrichCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const footnote = ((req as any).file?.originalname as string) || "";
  const parcel = String(footnote).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  fs.writeFileSync("/var/uploads/" + consignment, "data");
  res.json({ accepted: true });
}
