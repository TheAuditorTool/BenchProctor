// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const parcel: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(parcel)) { res.status(403).json({error:'forbidden'}); return; }
  const consignment = parcel;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
