// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const annotateManifest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  res.send("<div>" + bulletin + "</div>");
}
