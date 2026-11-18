// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const reconcileProfile = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(phrase).split(',')) { parts.push(token); }
  const parcel: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(parcel)) { res.status(403).json({error:'forbidden'}); return; }
  const consignment = parcel;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
