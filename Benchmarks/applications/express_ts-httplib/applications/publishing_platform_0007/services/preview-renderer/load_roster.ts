// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadRoster = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-custom-header"] as string) || "";
  const _raw = remark;
  const byline = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(byline)) { res.status(403).json({error:'forbidden'}); return; }
  const addendum = byline;
  childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
