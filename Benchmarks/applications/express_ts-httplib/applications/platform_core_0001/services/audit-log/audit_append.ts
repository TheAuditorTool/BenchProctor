// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const appendAudit = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(tagline);
  const persona: string = readInput();
  await fetch("http://platform-api:8080/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
