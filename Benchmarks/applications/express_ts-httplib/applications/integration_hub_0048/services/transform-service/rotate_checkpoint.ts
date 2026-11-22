// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["x-custom-header"] as string) || "";
  const _raw = citation;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const heading = handshake;
  childProcess.spawn("echo " + heading, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
