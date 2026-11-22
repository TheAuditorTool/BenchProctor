// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileComment = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body?.payload as string) || "";
  const synopsis = `${caption}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + synopsis + "</section>"); return;
}
