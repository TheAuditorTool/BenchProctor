// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers["x-custom-header"] as string) || "";
  const _raw = heading;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(addendum)) { res.status(403).json({error:'forbidden'}); return; }
  const byline = addendum;
  childProcess.spawn("echo " + byline, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
