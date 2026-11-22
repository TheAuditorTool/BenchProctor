// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  res.send("<div>" + consignment + "</div>");
}
