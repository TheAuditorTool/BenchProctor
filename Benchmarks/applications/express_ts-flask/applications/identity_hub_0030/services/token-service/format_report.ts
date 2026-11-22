// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const formatReport = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(tagline);
  res.send(shared.escapeHtml(persona));
}
