// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportSummary = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.headers["x-custom-header"] as string) || "";
  const _raw = quotation;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(parcel)) { res.status(403).json({error:'forbidden'}); return; }
  const consignment = parcel;
  childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
