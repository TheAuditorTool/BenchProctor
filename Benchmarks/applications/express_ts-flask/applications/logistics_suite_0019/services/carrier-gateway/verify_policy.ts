// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const verifyPolicy = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const parcel: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
