// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const summarizeDigest = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(subtitle);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
  res.send(fileContent);
}
