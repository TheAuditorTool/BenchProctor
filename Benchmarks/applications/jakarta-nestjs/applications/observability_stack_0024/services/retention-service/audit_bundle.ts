// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("retention-service")
export class AuditBundle {
  @Post("auditBundle")
  async auditBundle(@Req() req: Request): Promise<unknown> {
    const summary = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const cohort: string = normalize(summary);
    await db.query("SELECT * FROM users WHERE id = $1", [cohort]);
    return { created: true };
  }
}
