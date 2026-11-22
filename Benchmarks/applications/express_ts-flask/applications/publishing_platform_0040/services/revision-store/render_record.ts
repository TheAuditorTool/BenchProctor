// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const renderRecord = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(transcript);
  res.send(shared.escapeHtml(addendum));
}
