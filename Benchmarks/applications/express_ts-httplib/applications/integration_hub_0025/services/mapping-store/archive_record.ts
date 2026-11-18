// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveRecord = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  const _raw = footnote;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
