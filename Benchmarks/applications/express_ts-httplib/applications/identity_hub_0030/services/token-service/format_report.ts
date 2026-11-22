// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const formatReport = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body as string) || "";
  const persona = tagline != null ? tagline : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const note = persona;
  res.send("<div>" + note + "</div>");
}
