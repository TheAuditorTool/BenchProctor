// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pruneRoster = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const byline = footnote != null ? footnote : '';
  const addendum = byline.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + addendum + "</div>");
}
