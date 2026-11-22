// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderBundle = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(remark);
  JSON.parse(gauge);
  res.json({ accepted: true });
}
