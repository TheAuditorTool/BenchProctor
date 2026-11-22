// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const summarizeDigest = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers["x-forwarded-for"] as string) || "";
  const persona = subtitle != null ? subtitle : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ accepted: true });
}
