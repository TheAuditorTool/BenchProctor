// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishConfig = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers["x-custom-header"] as string) || "";
  const _raw = paragraph;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = persona;
  res.send("<div>" + synopsis + "</div>");
}
