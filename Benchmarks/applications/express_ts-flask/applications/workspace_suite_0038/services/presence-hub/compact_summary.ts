// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactSummary = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const remark: string = transform(preface);
  res.send("<div>" + remark + "</div>");
}
