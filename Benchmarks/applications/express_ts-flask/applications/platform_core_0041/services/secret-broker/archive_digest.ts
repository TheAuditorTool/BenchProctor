// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveDigest = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers["x-custom-header"] as string) || "";
  const _raw = passage;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  res.send("<div>" + handshake + "</div>");
}
