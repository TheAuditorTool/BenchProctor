// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const saveRevision = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(transcript);
  const addendum: string = readInput();
  await fetch("http://syndication-feed:8080/push_syndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ accepted: true });
}
