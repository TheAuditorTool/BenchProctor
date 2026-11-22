// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const enrichHeader = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const bulletin: string = transform(preface);
  res.send(shared.escapeHtml(bulletin));
}
