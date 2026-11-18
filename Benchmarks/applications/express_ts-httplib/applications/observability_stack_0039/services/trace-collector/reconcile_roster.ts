// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileRoster = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const cohort = caption != null ? caption : '';
  const gauge = cohort.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + gauge + "</div>");
}
