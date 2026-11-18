// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichLedger = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
