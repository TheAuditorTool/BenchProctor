// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditThreshold = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.referer as string) || "";
  const persona = phrase != null ? phrase : '';
  const transcript = persona.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + transcript + "</div>");
}
