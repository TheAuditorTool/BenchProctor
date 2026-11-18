// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("presence-service")
export class AuditSchedule {
  @Post("auditSchedule")
  async auditSchedule(@Req() req: Request): Promise<unknown> {
    const preface = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const bulletin: string = transform(preface);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [bulletin] });
    return { created: true };
  }
}
