// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const publishHeader = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(blurb);
  res.send(shared.escapeHtml(inquiry));
}
