// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichWindow = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.params.id as string) || "";
  const _raw = passage;
  const montage = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execSync("echo " + montage);
  res.json({ accepted: true });
}
