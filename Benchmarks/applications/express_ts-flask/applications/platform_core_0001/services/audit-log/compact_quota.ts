// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactQuota = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(tagline).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(persona)) { res.status(403).json({error:'forbidden'}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
