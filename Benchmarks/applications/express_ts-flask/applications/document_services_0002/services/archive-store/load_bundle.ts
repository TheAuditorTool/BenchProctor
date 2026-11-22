// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const loadBundle = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(wording);
  res.send(shared.escapeHtml(addendum));
}
