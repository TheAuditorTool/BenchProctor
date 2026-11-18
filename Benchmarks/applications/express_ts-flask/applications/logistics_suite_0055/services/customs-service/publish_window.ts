// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(consignment)) { res.status(403).json({error:'forbidden'}); return; }
  const parcel = consignment;
  childProcess.execSync("echo " + parcel);
  res.json({ accepted: true });
}
