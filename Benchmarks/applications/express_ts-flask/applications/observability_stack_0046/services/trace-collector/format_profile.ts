// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const formatProfile = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(paragraph);
  res.send(shared.escapeHtml(gauge));
}
