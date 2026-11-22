// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const exportReport = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const voucher: string = transform(subject);
  res.send(shared.escapeHtml(voucher));
}
