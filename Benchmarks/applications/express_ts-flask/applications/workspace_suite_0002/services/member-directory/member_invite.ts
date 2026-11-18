// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const inviteMember = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(transcript);
  const heading: string = readInput();
  await fetch("http://comment-service:8000/post_comment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: heading})});
  res.json({ accepted: true });
}
