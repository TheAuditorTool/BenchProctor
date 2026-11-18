// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("secret-broker")
export class NormalizeRoster {
  @Post("normalizeRoster")
  async normalizeRoster(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(passage);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [persona] });
    return { created: true };
  }
}
