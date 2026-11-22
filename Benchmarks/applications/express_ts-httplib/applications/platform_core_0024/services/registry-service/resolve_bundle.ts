// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveBundle = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers["x-custom-header"] as string) || "";
  const _raw = heading;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const persona = handshake;
  childProcess.spawn("echo " + persona, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
