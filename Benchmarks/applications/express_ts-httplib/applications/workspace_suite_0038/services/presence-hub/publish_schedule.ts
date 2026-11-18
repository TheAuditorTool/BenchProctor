// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishSchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const remark = preface != null ? preface : '';
  const wording = remark.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + wording + "</div>");
}
