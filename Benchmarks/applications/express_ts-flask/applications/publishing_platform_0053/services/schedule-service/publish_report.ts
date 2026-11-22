// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const publishReport = async (req: Request, res: Response): Promise<void> => {
  const note = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const byline: string = transform(note);
  res.send(shared.escapeHtml(byline));
}
