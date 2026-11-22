// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const renderLedger = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const restock: string = transform(excerpt);
  res.send(shared.escapeHtml(restock));
}
