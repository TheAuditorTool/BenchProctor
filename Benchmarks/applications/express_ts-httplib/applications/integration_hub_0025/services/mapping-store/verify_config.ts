// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifyConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(footnote);
  const blurb = handshake.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + blurb + "</div>");
}
