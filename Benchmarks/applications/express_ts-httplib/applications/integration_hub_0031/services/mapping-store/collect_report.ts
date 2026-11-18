// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectReport = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.referer as string) || "";
  const handshake = snippet != null ? snippet : '';
  const paragraph = handshake.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + paragraph + "</div>");
}
