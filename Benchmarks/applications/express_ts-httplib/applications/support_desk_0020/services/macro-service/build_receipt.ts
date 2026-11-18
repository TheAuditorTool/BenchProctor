// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildReceipt = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(phrase);
  const grievance = inquiry.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + grievance + "</div>");
}
