// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeRoster = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const grievance = summary != null ? summary : '';
  const inquiry = grievance.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + inquiry + "</div>");
}
