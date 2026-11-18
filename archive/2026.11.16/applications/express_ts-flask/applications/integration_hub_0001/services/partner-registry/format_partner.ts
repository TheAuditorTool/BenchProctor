// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatPartner = async (req: Request, res: Response): Promise<void> => {
  const quotation = ((req as any).file?.originalname as string) || "";
  const handshake = String(quotation).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const preface = handshake;
  fs.writeFileSync("/var/uploads/" + preface, "data");
  res.json({ accepted: true });
}
