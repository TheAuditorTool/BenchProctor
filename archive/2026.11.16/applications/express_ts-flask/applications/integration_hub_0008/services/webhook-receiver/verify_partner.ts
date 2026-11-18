// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifyPartner = async (req: Request, res: Response): Promise<void> => {
  const preface = ((req as any).file?.originalname as string) || "";
  const handshake = String(preface).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = handshake;
  fs.writeFileSync("/var/uploads/" + paragraph, "data");
  res.json({ accepted: true });
}
