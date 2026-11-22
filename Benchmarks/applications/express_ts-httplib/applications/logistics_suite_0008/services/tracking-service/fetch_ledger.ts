// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchLedger = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const consignment: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(consignment)) { res.status(403).json({error:'forbidden'}); return; }
  const parcel = consignment;
  childProcess.execSync("echo " + parcel);
  res.json({ accepted: true });
}
