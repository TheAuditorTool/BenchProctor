// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("member-directory")
export class AuditRoster {
  @Post("auditRoster")
  async auditRoster(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const heading: string = transform(transcript);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [heading] });
    return { created: true };
  }
}
