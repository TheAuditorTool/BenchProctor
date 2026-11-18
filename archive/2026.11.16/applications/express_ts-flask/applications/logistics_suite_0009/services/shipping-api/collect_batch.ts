// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectBatch = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(subject);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
