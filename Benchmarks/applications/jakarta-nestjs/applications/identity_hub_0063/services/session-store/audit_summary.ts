// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("session-store")
export class AuditSummary {
  @Post("auditSummary")
  async auditSummary(@Req() req: Request): Promise<unknown> {
    const paragraph = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(paragraph);
    await db.query("SELECT * FROM users WHERE id = $1", [persona]);
    return { created: true };
  }
}
