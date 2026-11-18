// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archivePolicy = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const restock = summary != null ? summary : '';
  const backorder = restock.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + backorder + "</div>");
}
