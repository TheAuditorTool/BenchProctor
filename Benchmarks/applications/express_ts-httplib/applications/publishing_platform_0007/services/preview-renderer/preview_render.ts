// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderPreview = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = remark;
  const byline: string = (globalThis as any).lastRequestValue;
  await fetch("http://revision-store:8080/save_revision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
