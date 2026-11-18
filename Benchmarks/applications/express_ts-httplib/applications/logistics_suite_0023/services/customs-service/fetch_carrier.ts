// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const fetchCarrier = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.authorization as string) || "";
  const _raw = caption;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(parcel);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const consignment = _parsed.data;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
