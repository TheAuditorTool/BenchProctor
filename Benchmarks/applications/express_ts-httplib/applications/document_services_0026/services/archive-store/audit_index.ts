// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditIndex = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body?.payload as string) || "";
  const addendum = `${preface}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + addendum + "</section>"); return;
}
