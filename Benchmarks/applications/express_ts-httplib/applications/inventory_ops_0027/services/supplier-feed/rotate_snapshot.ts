// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const restock: string = transform(summary);
  const backorder = restock.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + backorder + "</div>");
}
