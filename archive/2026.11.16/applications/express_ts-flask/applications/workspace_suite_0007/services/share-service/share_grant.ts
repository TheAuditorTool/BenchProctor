// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const grantShare = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).file?.originalname as string) || "";
  const subtitle = String(summary).slice(0, 200);
  await fetch("http://document-collab:8000/edit_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: subtitle})});
  res.json({ accepted: true });
}
