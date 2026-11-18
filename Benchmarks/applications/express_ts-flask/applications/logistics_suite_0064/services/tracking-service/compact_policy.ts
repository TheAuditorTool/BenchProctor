// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactPolicy = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers["x-custom-header"] as string) || "";
  const _raw = transcript;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(parcel))) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  res.send("<div>" + consignment + "</div>");
}
