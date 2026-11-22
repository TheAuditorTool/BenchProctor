// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderPreview = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const byline: string = readInput();
  await fetch("http://revision-store:8000/save_revision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
