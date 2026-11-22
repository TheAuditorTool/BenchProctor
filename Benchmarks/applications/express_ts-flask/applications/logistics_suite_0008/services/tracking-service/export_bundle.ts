// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportBundle = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.cookies?.session_token as string) || "";
  const _raw = caption;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(consignment))) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  childProcess.exec("echo " + parcel, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
