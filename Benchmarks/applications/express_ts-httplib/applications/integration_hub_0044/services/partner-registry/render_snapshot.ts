// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderSnapshot = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(blurb);
  const citation = handshake.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + citation + "</div>");
}
