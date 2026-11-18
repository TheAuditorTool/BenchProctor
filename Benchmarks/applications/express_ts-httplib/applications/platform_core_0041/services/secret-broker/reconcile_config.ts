// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileConfig = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  res.send("<div>" + handshake + "</div>");
}
