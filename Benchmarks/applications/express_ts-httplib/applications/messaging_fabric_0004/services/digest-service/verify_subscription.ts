// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySubscription = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const bulletin: string = transform(paragraph);
  const synopsis = bulletin.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + synopsis + "</div>");
}
