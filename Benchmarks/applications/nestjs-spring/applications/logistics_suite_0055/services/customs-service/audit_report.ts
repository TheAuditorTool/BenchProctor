// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class AuditReport {
  @Post("auditReport")
  async auditReport(@Req() req: Request): Promise<unknown> {
    const heading = (req.query.id as string) || "";
    const [consignment] = String(heading).split(',');
    return "<div>" + consignment + "</div>";
  }
}
