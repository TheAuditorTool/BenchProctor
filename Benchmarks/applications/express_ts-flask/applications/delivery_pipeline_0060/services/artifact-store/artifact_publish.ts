// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishArtifact = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(wording);
  const remark: string = readInput();
  await fetch("http://rollback-service:8000/trigger_rollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: remark})});
  res.json({ accepted: true });
}
