// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers["x-forwarded-for"] as string) || "";
  const handshake = heading != null ? heading : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  fs.writeFileSync("/var/uploads/" + persona, "data");
  res.json({ accepted: true });
}
