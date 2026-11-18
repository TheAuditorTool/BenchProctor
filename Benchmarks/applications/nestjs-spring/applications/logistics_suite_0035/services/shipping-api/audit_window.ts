// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("shipping-api")
export class AuditWindow {
  @Post("auditWindow")
  async auditWindow(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const parcel: string = transform(phrase);
    return "<div>" + parcel + "</div>";
  }
}
