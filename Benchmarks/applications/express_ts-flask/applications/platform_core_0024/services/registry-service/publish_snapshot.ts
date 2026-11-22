// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishSnapshot = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  res.send("<div>" + handshake + "</div>");
}
