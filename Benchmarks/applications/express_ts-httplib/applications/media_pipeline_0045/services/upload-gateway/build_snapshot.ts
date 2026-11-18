// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const buildSnapshot = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.params.id as string) || "";
  const _raw = notice;
  const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execSync("echo " + rendition);
  res.json({ accepted: true });
}
