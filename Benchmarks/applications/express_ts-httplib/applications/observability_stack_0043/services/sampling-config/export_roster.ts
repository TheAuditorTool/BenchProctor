// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportRoster = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  const gauge = note != null ? note : '';
  const cohort = gauge.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + cohort + "</div>");
}
