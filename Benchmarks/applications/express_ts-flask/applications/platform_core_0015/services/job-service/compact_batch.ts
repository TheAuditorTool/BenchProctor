// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactBatch = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const persona = handshake;
  childProcess.execSync("echo " + persona);
  res.json({ accepted: true });
}
