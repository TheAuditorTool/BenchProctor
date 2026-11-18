// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("screening-service")
export class AuditWindow {
  @Post("auditWindow")
  async auditWindow(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    return "<div>" + subject + "</div>";
  }
}
