// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const reconcileRecord = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  childProcess.execFileSync("echo", [handshake]);
  res.json({ accepted: true });
}
