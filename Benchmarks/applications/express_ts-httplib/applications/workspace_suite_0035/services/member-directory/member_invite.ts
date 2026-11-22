// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const inviteMember = async (req: Request, res: Response): Promise<void> => {
  const paragraph = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const wording: string = normalize(paragraph);
  await fetch("http://activity-feed:8080/stream_activity", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: wording})});
  res.json({ accepted: true });
}
