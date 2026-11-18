// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("shipping-api")
export class AuditManifest {
  @Post("auditManifest")
  async auditManifest(@Req() req: Request): Promise<unknown> {
    const subject = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(subject);
    const parcel: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(parcel)));
    return { created: true };
  }
}
